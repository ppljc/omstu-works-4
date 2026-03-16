namespace lab8_2;

public sealed class FTNGFaculty : FacultyBase
{
    private static readonly Lazy<FTNGFaculty> _instance = new Lazy<FTNGFaculty>(() => new FTNGFaculty());
    public static FTNGFaculty Instance => _instance.Value;

    public int DrillingSimulators { get; private set; }
    public int PartnerCompanies { get; private set; }

    private FTNGFaculty() : base(
        name: "ФТНГ (Факультет транспорта нефти и газа)",
        dean: "Квасов И. Н.",
        departments: 6,
        students: 850
    )
    {
        DrillingSimulators = 4;
        PartnerCompanies = 12;
    }

    public override double CalculateYearlyBudget()
    {
        double studentSubsidy = 60000;
        double simulatorMaintenance = 500000;
        double partnerGrants = PartnerCompanies * 200000;

        return (StudentCount * studentSubsidy) + (DrillingSimulators * simulatorMaintenance) + partnerGrants;
    }

    public override void PrintInfo()
    {
        base.PrintInfo();
        Console.WriteLine($"Industrial Stats: {DrillingSimulators} heavy simulators | {PartnerCompanies} partner companies.");
    }

    public void StartFieldPractice()
    {
        Console.WriteLine($"[FIELD] Students of {Name} are heading to the oil fields for practical training.");
    }
}