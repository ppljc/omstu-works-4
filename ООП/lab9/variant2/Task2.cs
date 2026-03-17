using System.Collections.Concurrent;

namespace lab9_2;

public class Task2
{
    public void Execute()
    {
        ConcurrentBag<string> pictures = [];
        string[] pictureExtensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"];

        List<Task> tasks = [];
        
        foreach (var drive in DriveInfo.GetDrives())
        {
            if (!drive.IsReady)
                continue;

            var root = drive.RootDirectory;
            
            tasks.Add(Task.Run(() =>
            {
                try
                {
                    var rootDirs = root.GetDirectories();

                    List<Task> subTasks = [];

                    foreach (var dir in rootDirs)
                    {
                        subTasks.Add(Task.Run(() =>
                        {
                            try
                            {
                                TraverseDirectory(dir, pictureExtensions, pictures);
                            }
                            catch (Exception ex)
                            {
                                Console.WriteLine($"Ошибка при обработке папки {dir}: {ex.Message}");
                            }
                        }));
                    }

                    Task.WaitAll(subTasks.ToArray());
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Ошибка при обработке диска {root}: {ex.Message}");
                }
            }));
        }

        Task.WaitAll(tasks.ToArray());

        var output = new FileInfo("pictures.txt");
        using (var writer = new StreamWriter(output.OpenWrite()))
        {
            foreach (var path in pictures)
                writer.WriteLine(path);
        }
    }

    private void TraverseDirectory(DirectoryInfo dir, string[] exts, ConcurrentBag<string> buffer)
    {
        FileInfo[] files;
        DirectoryInfo[] subdirs;

        try
        {
            files = dir.GetFiles();
            subdirs = dir.GetDirectories();
        }
        catch
        {
            return;
        }

        foreach (var file in files)
        {
            if (Array.Exists(exts, e => file.Extension.Equals(e, StringComparison.OrdinalIgnoreCase)))
            {
                buffer.Add(file.FullName);
                Console.WriteLine(file.FullName);
            }
        }

        foreach (var sub in subdirs)
            TraverseDirectory(sub, exts, buffer);
    }
}