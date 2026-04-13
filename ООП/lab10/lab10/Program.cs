namespace lab10;

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

internal static class Program
{
    private static void Main()
    {
        Console.WriteLine("Enter the path to the folder with audio files:");
        var inputFolder = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(inputFolder) || !Directory.Exists(inputFolder))
        {
            Console.WriteLine("The folder does not exist.");
            return;
        }

        var files = Directory.EnumerateFiles(inputFolder)
            .Where(IsAudioFile)
            .ToList();

        if (files.Count == 0)
        {
            Console.WriteLine("No audio files were found.");
            return;
        }

        var outputFolder = Path.Combine(inputFolder, "ProcessedAudio");
        var coreCount = Math.Max(1, GetPhysicalCoreCount());
        var workerCount = Math.Min(coreCount, files.Count);
        // var chunks = SplitIntoChunks(files, workerCount).ToList();
        var chunks = SplitIntoChunks(files, 2).ToList();

        Console.WriteLine($"Found {files.Count} audio files.");
        Console.WriteLine($"Using {workerCount} tasks.");
        Console.WriteLine("Press C to cancel after the current audio finishes.");

        using var cts = new CancellationTokenSource();
        var processedAudios = new ConcurrentBag<Audio>();

        var tasks = chunks.Select((chunk, index) =>
            Task.Run(() => ProcessChunk(chunk, index + 1, processedAudios, cts.Token), cts.Token))
            .ToArray();

        var cancellationMonitor = Task.Run(() => MonitorCancellation(cts), cts.Token);

        try
        {
            Task.WaitAll(tasks, cts.Token);
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Processing was cancelled.");
        }
        catch (AggregateException ex)
        {
            foreach (var inner in ex.Flatten().InnerExceptions)
            {
                if (inner is not OperationCanceledException)
                {
                    Console.WriteLine($"Task error: {inner.Message}");
                }
            }
        }

        cts.Cancel();
        try
        {
            cancellationMonitor.Wait(cts.Token);
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Processing was cancelled.");
        }

        Directory.CreateDirectory(outputFolder);

        foreach (var audio in processedAudios.OrderBy(a => a.FileName, StringComparer.OrdinalIgnoreCase))
        {
            try
            {
                audio.Save(outputFolder);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to save {audio.FileName}: {ex.Message}");
            }
        }

        Console.WriteLine($"Processing completed. Saved {processedAudios.Count} files to: {outputFolder}");
    }

    private static void ProcessChunk(
        IEnumerable<string> chunk,
        int taskNumber,
        ConcurrentBag<Audio> processedAudios,
        CancellationToken token)
    {
        foreach (var path in chunk)
        {
            if (token.IsCancellationRequested)
            {
                Console.WriteLine($"Task {taskNumber}: cancellation requested, stopping after the current audio.");
                break;
            }

            try
            {
                var audio = new Audio(path);
                audio.SlowDownBy2X(token);
                processedAudios.Add(audio);
                Console.WriteLine($"Task {taskNumber}: completed {audio.FileName}");
            }
            catch (OperationCanceledException)
            {
                Console.WriteLine($"Task {taskNumber}: cancelled {Path.GetFileName(path)}");
                break;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Task {taskNumber}: failed to process {Path.GetFileName(path)} - {ex.Message}");
            }
        }
    }

    private static void MonitorCancellation(CancellationTokenSource cts)
    {
        try
        {
            while (!cts.IsCancellationRequested)
            {
                if (!Console.KeyAvailable)
                {
                    Thread.Sleep(100);
                    continue;
                }

                var key = Console.ReadKey(true).Key;
                if (key == ConsoleKey.C)
                {
                    Console.WriteLine("Cancellation requested.");
                    cts.Cancel();
                    break;
                }
            }
        }
        catch
        {
            // ignored
        }
    }

    private static List<List<string>> SplitIntoChunks(List<string> items, int workers)
    {
        var result = new List<List<string>>();

        for (var i = 0; i < workers; i++)
        {
            result.Add([]);
        }

        for (var i = 0; i < items.Count; i++)
        {
            result[i % workers].Add(items[i]);
        }

        return result;
    }

    private static bool IsAudioFile(string path)
    {
        var ext = Path.GetExtension(path);

        return ext.Equals(".wav", StringComparison.OrdinalIgnoreCase)
            || ext.Equals(".mp3", StringComparison.OrdinalIgnoreCase)
            || ext.Equals(".flac", StringComparison.OrdinalIgnoreCase)
            || ext.Equals(".aac", StringComparison.OrdinalIgnoreCase)
            || ext.Equals(".ogg", StringComparison.OrdinalIgnoreCase)
            || ext.Equals(".m4a", StringComparison.OrdinalIgnoreCase);
    }

    private static int GetPhysicalCoreCount()
    {
        return Environment.ProcessorCount;
    }
}
