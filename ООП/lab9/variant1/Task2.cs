using System.Collections.Concurrent;

namespace lab9;

public class Task2
{
    public void Execute()
    {
        ConcurrentBag<string> docs = [];
        string[] docExtensions = [".doc", ".docx", ".pdf", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"];

        List<Task> tasks = [];

        foreach (var drive in DriveInfo.GetDrives())
        {
            if (!drive.IsReady)
                continue;

            var root = drive.RootDirectory.FullName;

            tasks.Add(Task.Run(() =>
            {
                try
                {
                    var rootDirs = Directory.GetDirectories(root);

                    List<Task> subTasks = [];

                    foreach (var dir in rootDirs)
                    {
                        subTasks.Add(Task.Run(() =>
                        {
                            try
                            {
                                TraverseDirectory(dir, docExtensions, docs);
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

        File.WriteAllLines("docs.txt", docs);
    }

    private void TraverseDirectory(string path, string[] exts, ConcurrentBag<string> buffer)
    {
        string[] files;
        string[] subdirs;

        try
        {
            files = Directory.GetFiles(path);
            subdirs = Directory.GetDirectories(path);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка доступа к {path}: {ex.Message}");
            return;
        }

        foreach (var f in files)
        {
            var ext = Path.GetExtension(f);
            if (Array.Exists(exts, e => string.Equals(ext, e, StringComparison.OrdinalIgnoreCase)))
            {
                buffer.Add(f);
                Console.WriteLine(f);
            }
        }

        foreach (var sub in subdirs)
            TraverseDirectory(sub, exts, buffer);
    }
}