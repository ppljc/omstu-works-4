using lab_7;

namespace tests;

public class DifferenceTests
{
    private MyDel _difference;

    [SetUp]
    public void Setup()
    {
        _difference = ArrayDifference.Create();
    }

    [TestCase(new int[] {1, 2, 3, 4, 5, 6, 7, 8}, 7)]
    [TestCase(new int[] {6, 23, 3, 4, 5, 6, 7, 8}, 20)]
    [TestCase(new int[] {6, 0, 3, 4, 10, 6, 7, 1}, 10)]
    [TestCase(new int[] {5}, 0)]
    [TestCase(new int[] {5, 5, 5, 5, 5}, 0)]
    [TestCase(new int[] {-10, -15, -20, -25, -30}, 20)]
    [TestCase(new int[] {-10, 0, -20, 30, 40}, 60)]
    [TestCase(new int[] {0, 0, 0, 0}, 0)]
    [TestCase(new int[] {-1, 0, 0, 0}, 1)]
    public void Test_Normal(int[] array, double result)
    {
        Assert.That(_difference.Invoke(array), Is.EqualTo(result));
    }

    [Test]
    public void Test_Empty()
    {
        int[] array = [];
        Assert.Throws<ArgumentException>(() => _difference.Invoke(array));
    }
}