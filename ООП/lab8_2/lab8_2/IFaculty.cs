namespace lab8_2;

public interface IFaculty
{
    string Name { get; }
    string Dean { get; }
    int Departments { get; }
    int StudentCount { get; } // Добавим количество студентов
    void PrintInfo();
    double CalculateYearlyBudget(); // Метод для расчета бюджета
}