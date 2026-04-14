namespace lab10;

using System;
using System.IO;
using System.Threading;

public class Audio
{
    public string SourcePath { get; }
    public string FileName { get; }
    public byte[] Data { get; private set; }

    public Audio(string sourcePath)
    {
        SourcePath = sourcePath ?? throw new ArgumentNullException(nameof(sourcePath));
        FileName = Path.GetFileName(sourcePath);
        Data = File.ReadAllBytes(sourcePath);
    }

    public void SlowDownBy2X(CancellationToken token)
    {
        token.ThrowIfCancellationRequested();
        
        Thread.Sleep(1000);

        var source = Data;
        var slowed = new byte[source.Length * 2];

        Buffer.BlockCopy(source, 0, slowed, 0, source.Length);
        Buffer.BlockCopy(source, 0, slowed, source.Length, source.Length);

        Data = slowed;
    }

    public void Save(string outputDirectory)
    {
        // Directory.CreateDirectory(outputDirectory);
        var targetPath = Path.Combine(outputDirectory, FileName);
        File.WriteAllBytes(targetPath, Data);
    }
}
