using System;

namespace lab8_2;

public sealed class FIFaculty : FacultyBase
{
    private static readonly Lazy<FIFaculty> _instance = new Lazy<FIFaculty>(() => new FIFaculty());
    public static FIFaculty Instance => _instance.Value;

    public int ComputerLabs { get; private set; }

    private FIFaculty() : base(
        name: "ФИТиКС (Факультет информационных технологий и компьютерных систем)",
        dean: "Грицай А. С.",
        departments: 6,
        students: 1200
    )
    {
        ComputerLabs = 15;
    }

    public override double CalculateYearlyBudget()
    {
        double baseRate = 50000;
        double labMaintenance = 150000;
        return (StudentCount * baseRate) + (ComputerLabs * labMaintenance);
    }

    public override void PrintInfo()
    {
        base.PrintInfo();
        Console.WriteLine($"Tech Infrastructure: {ComputerLabs} specialized computer labs.");
    }

    public void OrganizeHackathon()
    {
        Console.WriteLine($"[EVENT] {Name} is starting a 48-hour hackathon for {StudentCount} students!");
    }
}