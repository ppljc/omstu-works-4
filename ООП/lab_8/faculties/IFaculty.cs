namespace faculties;

public interface IFaculty
{
    string Name { get; }
    string Dean { get; }
    int Departments { get; }
    void PrintInfo();
}