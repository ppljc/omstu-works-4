using System.Text;

namespace lab_6;

public class GameConsole : IConsole, IHack
{
    public ProcessorType Processor { get; set; }
    public int CpuClockMHz { get; set; }
    public ManufacturerName ManufacturerName { get; set; }
    public MediaType Media { get; set; }
    public string Model { get; set; }
    public int RAMSizeGb { get; set; }
    public int HardDriveSizeGb { get; set; }
    public List<string> InstalledGames { get; set; } = [];
    public List<string> Accounts { get; set; } = [];
    
    public GameConsole() { }
    
    public GameConsole(ProcessorType proc, int clock, ManufacturerName man, MediaType med, string model, int ram, int storage)
    {
        Processor = proc;
        CpuClockMHz = clock;
        ManufacturerName = man;
        Media = med;
        Model = model;
        RAMSizeGb = ram;
        HardDriveSizeGb = storage;
    }

    private static readonly Random Random = new Random();
    
    public bool TrySoftwareHack()
    {
        var hackSuccessChances = this.ManufacturerName switch
        {
            ManufacturerName.Microsoft => 30,
            ManufacturerName.Nintendo => 40,
            ManufacturerName.Sega => 70,
            ManufacturerName.Sony => 33,
            ManufacturerName.Valve => 5,
            ManufacturerName.Lenovo => 99,
            _ => 50
        };
        
        var success = Random.Next(0, 100) < hackSuccessChances;
        
        Console.WriteLine(success
            ? "Console successfully hacked. Steal everything!"
            : "ERROR: Try to inject virus to console failed. Console called police!");

        return success;
    }

    public bool TryHardwareHack()
    {
        var hackSuccessChances = this.Media switch
        {
            MediaType.Cartridge => 41,
            MediaType.BluRay    => 30,
            MediaType.CD        => 33,
            MediaType.DVD       => 29,
            MediaType.Flash     => 13,
            _                   => 50
        };
        
        var success = Random.Next(0, 100) < hackSuccessChances;
        
        Console.WriteLine(success
            ? "You hacked storage system. Load any game!"
            : "ERROR: Console`s hardware detected your penetration. Leave country as soon as you can!");
        
        return success;
    }

    private static readonly string[] AvailableGames =
    [
        "GTA 5", "GTA 4", "CS2", "Dota 2", "Everlasting Summer", "League Of Legends", "Minecraft", "Forza Horizon 5",
        "Elden Ring", "Dark Souls 4", "BeamNG.Drive", "The Crew 2", "The Last of Us", "The Legend of Zelda"
    ];

    private const string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_";
    
    public static GameConsole Generate()
    {
        var manufacturer = (ManufacturerName)Random.Next(0, 6);
        
        var model = manufacturer switch
        {
            ManufacturerName.Microsoft => "Xbox " + (Random.Next(0, 2) == 0 ? "Series S" : "Series X"),
            ManufacturerName.Nintendo  => "Nintendo " + (Random.Next(0, 2) == 0 ? "Switch" : "Switch 2"),
            ManufacturerName.Sony      => "Playstation " + Random.Next(1, 5),
            ManufacturerName.Sega      => "Dreamcast",
            ManufacturerName.Valve     => "Steam " + (Random.Next(0, 2) == 0 ? "Deck" : "Machine"),
            ManufacturerName.Lenovo    => "Legion Go",
            _                          => "Unknown"
        };

        var console = new GameConsole(
            (ProcessorType)Random.Next(0, 4),
            Random.Next(800, 4936),
            manufacturer,
            (MediaType)Random.Next(0, 5),
            model,
            Random.Next(1, 16),
            Random.Next(120, 1024)
        );

        var gamesAmount = Random.Next(0, 4);
        for (var i = 0; i < gamesAmount; i++)
        {
            var game = AvailableGames[Random.Next(0, 8)];
            
            if (!console.InstalledGames.Contains(game))
                console.InstalledGames.Add(game);
        }

        var accountsAmount = Random.Next(1, 3);
        for (var i = 0; i < accountsAmount; i++)
        {
            var accountNameLenght = Random.Next(8, 27);
            var accountName = new StringBuilder();

            for (var j = 0; j < accountNameLenght; j++)
            {
                var randomChar = Alphabet[Random.Next(Alphabet.Length)];
                accountName.Append(randomChar);
            }
            
            console.Accounts.Add(accountName.ToString());
        }

        return console;
    }

    public static List<GameConsole> Generate100()
    {
        var consoles = new List<GameConsole>();
        
        for (var i = 0; i < 100; i++)
        {
            consoles.Add(Generate());
        }

        return consoles;
    }
}