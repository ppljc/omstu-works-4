namespace faculties;

public sealed class FIFaculty : FacultyBase
{
    private static readonly Lazy<FIFaculty> _instance = new Lazy<FIFaculty>(() => new FIFaculty());

    public static FIFaculty Instance => _instance.Value;

    private FIFaculty()
    {
        Name = "ФИТиКС (Факультет информационных технологий и компьютерных систем)";
        Dean = "Грицай А. С.";
        Departments = 6;
    }
}