using lab_6;

namespace tests;

[TestFixture]
public class StringExtensionTests
{
    [TestCase("Hello234привет", "234привет")]
    [TestCase("Hola amigos", " ")]
    [TestCase("PrivetAndrey", "")]
    [TestCase("Вот те нате", "Вот те нате")]
    [TestCase("17.02.2026", "17.02.2026")]
    [TestCase("", "")]
    [TestCase("What about 123!@#$%^&*()?", "  123!@#$%^&*()?")]
    public void Test_RemoveLatinLetters(string input, string expected)
    {
        var output = input.RemoveLatinLetters();
        
        Assert.That(output, Is.EqualTo(expected));
    }
}