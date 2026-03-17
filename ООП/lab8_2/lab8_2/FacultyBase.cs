namespace lab8_2;

public abstract class FacultyBase : IFaculty
{
    public string Name { get; protected set; }
    public string Dean { get; protected set; }
    public int Departments { get; protected set; }
    public int StudentCount { get; protected set; }

    protected FacultyBase(string name, string dean, int departments, int students)
    {
        Name = name;
        Dean = dean;
        Departments = departments;
        StudentCount = students;
    }

    public virtual void PrintInfo()
    {
        Console.WriteLine($"--- Faculty: {Name} ---");
        Console.WriteLine($"Dean: {Dean} | Depts: {Departments} | Students: {StudentCount}");
    }

    public abstract double CalculateYearlyBudget();
    
    public virtual void HoldConference()
    {
        Console.WriteLine($"{Name} is holding a general academic conference.");
    }
}