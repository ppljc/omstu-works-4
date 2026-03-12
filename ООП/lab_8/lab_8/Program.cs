using System.Reflection;

namespace lab_8;

using lab8_lib;

public class Program
{
    static void Main()
    {
        var building = new Building();
        
        Console.WriteLine($"Building: {building.Name} at {building.address}.");

        var type = typeof(Building);
        
        Console.WriteLine($"\n{type.FullName}"); // инфа о классе
        
        Console.WriteLine("\nFields before:");
        foreach (var field in  type.GetFields())
        {
            Console.WriteLine($"{field.FieldType.Name} {field.Name} {field.GetValue(building)}");
        }

        var fieldAddress = type.GetField("address");
        
        fieldAddress?.SetValue(building, "Not here");
        
        Console.WriteLine($"\nField after:\n{fieldAddress?.FieldType.Name} {fieldAddress?.Name} {fieldAddress?.GetValue(building)}");
        
        Console.WriteLine("\nProperties before:");
        foreach (var property in  type.GetProperties())
        {
            Console.WriteLine($"{property.PropertyType.Name} {property.Name} {property.GetValue(building)}");
        }

        var propertyName = type.GetProperty("Name");
        
        propertyName?.SetValue(building, "Fufelschmerz State Building");
        
        Console.WriteLine($"\nProperty after:\n{propertyName?.PropertyType.Name} {propertyName?.Name} {propertyName?.GetValue(building)}");
        
        Console.WriteLine("\nMethods:");
        foreach (var method in  type.GetMethods())
        {
            Console.WriteLine($"{method.ReturnType.Name} {method.Name}");
        }
        
        var obj = Activator.CreateInstance(type);                                // использование конструктора
        Console.WriteLine($"\n{type.GetMethod("Demolish")?.Invoke(obj, null)}");  // вызов метода (просто пункты рядом в одно решение уместились)
        
        
    }
}