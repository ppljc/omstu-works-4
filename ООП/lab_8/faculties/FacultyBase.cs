namespace faculties;

public abstract class FacultyBase : IFaculty
{
    public string Name { get; protected set; }
    public string Dean { get; protected set; }
    public int Departments { get; protected set; }
    public void PrintInfo()
    {
        Console.WriteLine($"Faculty: {Name} | Dean: {Dean} | Departments: {Departments}");
    }
}