namespace lab8_2;

public class Program
{
    static void Main()
    {
        var fi = FIFaculty.Instance;
        var ftng = FTNGFaculty.Instance;
        var rtf = RTFFaculty.Instance;
        
        fi.PrintInfo();
        ftng.PrintInfo();
        rtf.PrintInfo();
    }
}