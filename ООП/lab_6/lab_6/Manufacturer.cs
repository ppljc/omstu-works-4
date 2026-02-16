namespace lab_6;

public class Manufacturer
{
    public string Name { get; set; }
    public Country Country { get; set; }
    public int EmployeeCount { get; set; }
    
    public Manufacturer() {}

    public Manufacturer(string name, Country country, int employee)
    {
        Name = name;
        Country = country;
        EmployeeCount = employee;
    }
}