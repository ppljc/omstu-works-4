using System.Collections.Concurrent;

namespace lab9_2;

public class Task2
{
    public void Execute()
    {
        ConcurrentBag<string> pictures = [];
        string[] pictureExtensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"];

        List<Thread> threads = [];

        foreach (var drive in DriveInfo.GetDrives())
        {
            Console.WriteLine(drive);
            try
            {
                var root = drive.RootDirectory;

                var rootDirs = root.GetDirectories();

                foreach (var dir in rootDirs)
                {
                    Console.WriteLine(dir);
                }
            }
            catch
            {
                continue;
            }
        }

        // Console.ReadKey();

        List<DirectoryInfo> dirs = [];
        
        foreach (var drive in DriveInfo.GetDrives())
        {
            if (!drive.IsReady)
                continue;

            var root = drive.RootDirectory;
            
            dirs.Add(root);
            
            var thread = new Thread(() =>
            {
                try
                {
                    var rootDirs = root.GetDirectories();

                    List<Thread> subThreads = [];

                    foreach (var dir in rootDirs)
                    {
                        if (dirs.Contains(dir))
                            continue;
                        
                        var subThread = new Thread(() =>
                        {
                            try
                            {
                                TraverseDirectory(dir, pictureExtensions, pictures);
                            }
                            catch (Exception ex)
                            {
                                Console.WriteLine($"Ошибка при обработке папки {dir}: {ex.Message}");
                            }
                        });
                        
                        subThreads.Add(subThread);
                        subThread.Start();
                    }

                    foreach (var subThread in subThreads)
                    {
                        subThread.Join();
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Ошибка при обработке диска {root}: {ex.Message}");
                }
            });
            
            threads.Add(thread);
            thread.Start();
        }

        foreach (var thread in threads)
        {
            thread.Join();
        }

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