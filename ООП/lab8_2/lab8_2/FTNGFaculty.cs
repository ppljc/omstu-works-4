namespace lab8_faculties;

public class FTNGFaculty : FacultyBase
{
    private static readonly Lazy<FTNGFaculty> _instance = new Lazy<FTNGFaculty>(() => new FTNGFaculty());

    public static FTNGFaculty Instance => _instance.Value;

    private FTNGFaculty()
    {
        Name = "ФТНГ (Факультет транспорта нефти и газа)";
        Dean = "Квасов И. Н.";
        Departments = 6;
    }
}