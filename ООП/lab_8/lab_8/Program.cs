namespace lab_8;

public class Program
{
    static void Main()
    {
        var building = new Building();
        
        Console.WriteLine($"Building: {building.Name} at {building.address}.");
    }
}