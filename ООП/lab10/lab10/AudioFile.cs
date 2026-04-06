namespace lab10;
using NAudio.Wave;
using NAudio.Lame;
using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

class AudioFile
{
    public string PathFile { get; }
    public string Name => System.IO.Path.GetFileName(PathFile);

    public AudioFile(string path) => PathFile = path;

    public async Task ChangeSpeedAsync(double speed, string outputDir, CancellationToken token)
    {
        using var reader = new AudioFileReader(PathFile);
        var outFile = Path.Combine(outputDir, Name);

        var newRate = (int)(reader.WaveFormat.SampleRate * speed);
        var newFormat = new WaveFormat(newRate, reader.WaveFormat.BitsPerSample, reader.WaveFormat.Channels);

        using var resampler = new MediaFoundationResampler(reader, newFormat);
        WaveFileWriter.CreateWaveFile(outFile, resampler);

        Console.WriteLine($"[{Name}] speed changed");
        await Task.CompletedTask;
    }

    public async Task InvertSamplesAsync(string outputDir, CancellationToken token)
    {
        string outFile = Path.Combine(outputDir, Name);

        using var reader = new WaveFileReader(PathFile);
        using var writer = new WaveFileWriter(outFile, reader.WaveFormat);

        float[] buffer = new float[reader.WaveFormat.SampleRate];
        var floatReader = new WaveChannel32(reader);

        int read;
        while ((read = floatReader.Read(buffer, 0, buffer.Length)) > 0)
        {
            token.ThrowIfCancellationRequested();
            for (int i = 0; i < read; i++) buffer[i] = -buffer[i];
            writer.WriteSamples(buffer, 0, read);
        }

        Console.WriteLine($"[{Name}] samples inverted");
        await Task.CompletedTask;
    }

    public async Task ConvertMp3ToWavAsync(string outputDir, CancellationToken token)
    {
        if (!Name.EndsWith(".mp3", StringComparison.OrdinalIgnoreCase)) return;

        string outFile = Path.Combine(outputDir, System.IO.Path.ChangeExtension(Name, ".wav"));
        using var reader = new Mp3FileReader(PathFile);
        WaveFileWriter.CreateWaveFile(outFile, reader);

        Console.WriteLine($"[{Name}] MP3 -> WAV");
        await Task.CompletedTask;
    }

    public async Task ConvertWavToMp3Async(string outputDir, CancellationToken token)
    {
        if (!Name.EndsWith(".wav", StringComparison.OrdinalIgnoreCase)) return;

        string outFile = Path.Combine(outputDir, System.IO.Path.ChangeExtension(Name, ".mp3"));
        using var reader = new AudioFileReader(PathFile);
        using var writer = new LameMP3FileWriter(outFile, reader.WaveFormat, LAMEPreset.STANDARD);

        await reader.CopyToAsync(writer, token);
        Console.WriteLine($"[{Name}] WAV -> MP3");
    }
}