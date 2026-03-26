using NAudio.Wave;
using NAudio.Lame;

namespace lab10;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("Enter audio folder path:");
        string inputDir = Console.ReadLine();

        if (!Directory.Exists(inputDir))
        {
            Console.WriteLine("Invalid path");
            return;
        }

        Console.WriteLine("1 Change speed\n2 Invert samples\n3 MP3 -> WAV\n4 WAV -> MP3");
        int choice = int.Parse(Console.ReadLine());

        double speedFactor = 1.0;
        if (choice == 1)
        {
            Console.WriteLine("Enter speed factor (e.g. 1.5):");
            speedFactor = double.Parse(Console.ReadLine());
        }

        string outputDir = Path.Combine(inputDir, "Processed");
        Directory.CreateDirectory(outputDir);

        var files = Directory.GetFiles(inputDir)
                             .Where(f => f.EndsWith(".wav", StringComparison.OrdinalIgnoreCase)
                                      || f.EndsWith(".mp3", StringComparison.OrdinalIgnoreCase))
                             .ToList();

        var globalCts = new CancellationTokenSource();
        var tasks = new List<Task>();

        Task.Run(() =>
        {
            while (!globalCts.IsCancellationRequested)
            {
                var key = Console.ReadKey(true).KeyChar;
                if (key == 'c')
                {
                    Console.WriteLine("\n1 Cancel current, 2 Cancel all");
                    var k = Console.ReadKey(true).KeyChar;
                    if (k == '2')
                    {
                        globalCts.Cancel();
                        Console.WriteLine("GLOBAL CANCEL");
                    }
                }
            }
        });

        foreach (var file in files)
        {
            tasks.Add(Task.Run(async () =>
            {
                var audio = new AudioFile(file);
                var cts = CancellationTokenSource.CreateLinkedTokenSource(globalCts.Token);
                try
                {
                    switch (choice)
                    {
                        case 1:
                            await audio.ChangeSpeedAsync(speedFactor, outputDir, cts.Token);
                            break;
                        case 2:
                            await audio.InvertSamplesAsync(outputDir, cts.Token);
                            break;
                        case 3:
                            await audio.ConvertMp3ToWavAsync(outputDir, cts.Token);
                            break;
                        case 4:
                            await audio.ConvertWavToMp3Async(outputDir, cts.Token);
                            break;
                    }
                }
                catch (OperationCanceledException)
                {
                    Console.WriteLine($"[CANCELLED] {audio.Name}");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"[ERROR] {audio.Name}: {ex.Message}");
                }

            }, globalCts.Token));
        }

        try
        {
            await Task.WhenAll(tasks);
            Console.WriteLine("[DONE]");
        }
        catch
        {
            Console.WriteLine("[STOPPED]");
        }
    }
}