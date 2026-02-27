namespace lab_7;

public static class Program
{
    public static void Main()
    {
        int[] numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8];

        var processor = ArrayDifference.Create();
        var result = processor.Invoke(numbers);
        
        Console.WriteLine($"Difference: {result}");
    }
}
