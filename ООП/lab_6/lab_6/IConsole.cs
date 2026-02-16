namespace lab_6;

public interface IConsole
{
    ProcessorType Processor { set; get; }
    int CpuClockMHz { get; set; }
    ManufacturerName ManufacturerName { set; get; }
    MediaType Media { set; get; }
    string Model { set; get; }
    int RAMSizeGb { get; set; }
    int HardDriveSizeGb { set; get; }
    List<string> InstalledGames { set; get; }
    List<string> Accounts { set; get; }
}
