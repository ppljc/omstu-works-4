namespace lab_6;

public interface IManufacturer
{
    string Name { get; set; }
    Country Country { get; set; }
    int EmployeeCount { get; set; }
}