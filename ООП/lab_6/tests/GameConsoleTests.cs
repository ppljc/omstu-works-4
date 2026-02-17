using lab_6;

namespace tests;

[TestFixture]
public class GameConsoleTests
{
    [Test]
    [Repeat(100)]
    public void Test_GameConsoleGenerate()
    {
        var console = GameConsole.Generate();
        
        Assert.Multiple(() =>
        {
            Assert.That(console.CpuClockMHz, Is.GreaterThan(0));
            Assert.That(console.Model, Is.Not.Null.Or.Empty);
            Assert.That(console.RAMSizeGb, Is.GreaterThan(0));
            Assert.That(console.HardDriveSizeGb, Is.GreaterThan(0));
            Assert.That(console.InstalledGames, Has.Count.GreaterThanOrEqualTo(0));
            Assert.That(console.Accounts, Is.Not.Empty);
        });
    }

    [Test]
    public void Test_GameConsoleGenerate100()
    {
        var consoles = GameConsole.Generate100();
        
        Assert.That(consoles, Has.Count.EqualTo(100));
    }
}