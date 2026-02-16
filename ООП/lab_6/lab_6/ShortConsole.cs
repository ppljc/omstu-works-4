namespace lab_6;

public class ShortConsole
{
    public int CpuClockMHz { get; set; }
    public int HardDriveSizeGb { get; set; }
    public List<string> Accounts { get; set; } = [];

    public ShortConsole(int clock, int storage, List<string> accounts)
    {
        CpuClockMHz = clock;
        HardDriveSizeGb = storage;
        Accounts = accounts;
    }
}