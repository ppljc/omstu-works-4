namespace faculties;

public class RTFFaculty : FacultyBase
{
    private static readonly Lazy<RTFFaculty> _instance = new Lazy<RTFFaculty>(() => new RTFFaculty());

    public static RTFFaculty Instance => _instance.Value;

    private RTFFaculty()
    {
        Name = "РТФ (Радиотехнический факультет)";
        Dean = "Кропачев Д. Ю.";
        Departments = 5;
    }
}