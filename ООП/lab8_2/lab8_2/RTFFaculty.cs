namespace lab8_2;

public sealed class RTFFaculty : FacultyBase
{
    private static readonly Lazy<RTFFaculty> _instance = new Lazy<RTFFaculty>(() => new RTFFaculty());
    public static RTFFaculty Instance => _instance.Value;

    public int LabStations { get; private set; }

    private RTFFaculty() : base(
        name: "РТФ (Радиотехнический факультет)",
        dean: "Кропачев Д. Ю.",
        departments: 5,
        students: 700 
    )
    {
        LabStations = 24;
    }

    public override double CalculateYearlyBudget()
    {
        double studentBase = 45000;
        double equipmentCalibration = LabStations * 25000;

        return (StudentCount * studentBase) + equipmentCalibration;
    }

    public override void PrintInfo()
    {
        base.PrintInfo();
        Console.WriteLine($"Hardware Stats: {LabStations} measurement stations");
    }

    public void CalibrateRadioEquipment()
    {
        Console.WriteLine($"[MAINTENANCE] {Name} is calibrating oscilloscopes and signal generators...");
    }
}