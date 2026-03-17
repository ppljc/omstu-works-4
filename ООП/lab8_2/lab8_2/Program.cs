namespace lab8_2;

public class Program
{
    static void Main()
    {
        Console.WriteLine("key press");
        Console.ReadKey();
        
        var fi = FIFaculty.Instance;
        var ftng = FTNGFaculty.Instance;
        var rtf = RTFFaculty.Instance;

        var fi2 = FIFaculty.Instance;
        
        Console.WriteLine(fi.Equals(fi2).ToString());
        fi.PrintInfo();
        ftng.PrintInfo();
        rtf.PrintInfo();
        
        Console.WriteLine("key press");
        Console.ReadKey();
    }
}