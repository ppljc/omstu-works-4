namespace lab_6;

class Program
{
    static void Main(string[] args)
    {
        // consoles generation
        var consoles = GameConsole.Generate100();
        foreach (var console in consoles)
        {
            Console.WriteLine(
                $"Console: Model - {console.Model}, Processor - {console.Processor}, MediaType - {console.Media}, RAM - {console.RAMSizeGb}GB, HDD - {console.HardDriveSizeGb}GB, Games - {console.InstalledGames.Count}, Accounts - {console.Accounts.Count}.");
        }
        
        Console.WriteLine(consoles[0].TryHardwareHack());
        Console.WriteLine(consoles[1].TrySoftwareHack());
        
        // manufacturers list
        var manufacturers = new List<Manufacturer>{
            new Manufacturer("Sony", Country.Japan, 110000),
            new Manufacturer("Microsoft", Country.USA, 220000),
            new Manufacturer("Nintendo", Country.Japan, 7000),
            new Manufacturer("Sega", Country.Japan, 3000),
            new Manufacturer("Valve", Country.France, 1000)
        };
        
        // 2
        // filtering consoles by processor
        // var armConsoles = new List<GameConsole>();
        // foreach (var console in consoles)
        // {
        //     if (console.Processor is ProcessorType.Armv8 or ProcessorType.Armv7)
        //     {
        //         armConsoles.Add(console);
        //     }
        // }
        var armConsoles = consoles
            .Where(c => c.Processor is ProcessorType.Armv8 or ProcessorType.Armv7).ToList();
        foreach (var console in armConsoles)
        {
            Console.WriteLine($"Arm console: Model - {console.Model}, Processor - {console.Processor}.");
        }
        
        // filtering consoles by processor and manufacturer
        // var x86SonyConsoles = new List<GameConsole>();
        // foreach (var console in consoles)
        // {
        //     if (console.Processor == ProcessorType.X86 && console.Manufacturer == Manufacturer.Sony)
        //     {
        //         x86SonyConsoles.Add(console);
        //     }
        // }
        var x86SonyConsoles = consoles
            .Where(c => c.Processor is ProcessorType.X86 && c.ManufacturerName is ManufacturerName.Sony).ToList();
        foreach (var console in x86SonyConsoles)
        {
            Console.WriteLine(
                $"X86 Sony console: Model - {console.Model}, Processor - {console.Processor}.");
        }
        
        // filtering consoles by owners game collection and ram
        // var minecraft4GBConsoles = new List<GameConsole>();
        // foreach (var console in minecraft4GBConsoles)
        // {
        //     if (console.InstalledGames.Contains("Minecraft") && console.RAMSizeGb >= 4)
        //     {
        //         minecraft4GBConsoles.Add(console);
        //     }
        // }
        var minecraft4GBConsoles = consoles.Where(c => c.InstalledGames.Contains("Minecraft") && c.RAMSizeGb >= 4).ToList();
        foreach (var console in minecraft4GBConsoles)
        {
            Console.WriteLine($"4GB RAM console with Minecraft: Model - {console.Model}, Games - [" +
                              string.Join(", ", console.InstalledGames) + "]");
            // Console.Write(
            //     $"4GB RAM console with Minecraft: Model - {console.Model}, Games - [ ");
            // foreach (var game in console.InstalledGames)
            // {
            //     Console.Write($"{game} ");
            // }
            // Console.Write("].\n");
        }
        
        // 3
        // sorting by processor
        // var n = consoles.Count; // bubble sort
        // for (var i = 0; i < n - 1; i++)
        // {
        //     for (var j = 0; j < n - i - 1; j++)
        //     {
        //         if (consoles[j].Processor > consoles[j + 1].Processor)
        //         {
        //             var temp = consoles[j];
        //             consoles[j] = consoles[j + 1];
        //             consoles[j + 1] = temp;
        //         }
        //     }
        // }
        var processorSortedConsoles = consoles.OrderBy(c => c.Processor).ToList();
        foreach (var console in processorSortedConsoles)
        {
            Console.WriteLine(
                $"Sorted by processor console: Model - {console.Model}, Processor - {console.Processor}.");
        }
        
        // sorting by processor and manufacturer
        // var n = consoles.Count; // bubble sort
        // for (var i = 0; i < n - 1; i++)
        // {
        //     for (var j = 0; j < n - i - 1; j++)
        //     {
        //         var needSwap = false;
        //
        //         if (consoles[j].Processor > consoles[j + 1].Processor)
        //         {
        //             needSwap = true;
        //         }
        //         else if (consoles[j].Processor == consoles[j + 1].Processor)
        //         {
        //             if (consoles[j].Manufacturer > consoles[j + 1].Manufacturer)
        //             {
        //                 needSwap = true;
        //             }
        //         }
        //
        //         if (needSwap)
        //         {
        //             var temp = consoles[j];
        //             consoles[j] = consoles[j + 1];
        //             consoles[j + 1] = temp;
        //         }
        //     }
        // }
        var consoleManufacturerSortedConsoles = consoles.OrderBy(c => c.Processor).ThenBy(c => c.ManufacturerName).ToList();
        foreach (var console in consoleManufacturerSortedConsoles)
        {
            Console.WriteLine(
                $"Sorted by processor and then manufacturer console: Processor - {console.Processor}, Manufacturer - {console.ManufacturerName}.");
        }
        
        // 4
        // select with cpu clock, hdd volume, accounts
        // var shortConsoles = new List<ShortConsole>();
        // foreach (var console in consoles)
        // {
        //     var shortConsole = new ShortConsole(console.CpuClockMHz, console.HardDriveSizeGb, console.Accounts);
        //     shortConsoles.Add(shortConsole);
        // }
        var shortConsoles = consoles.Select(c => new
        {
            CpuClockMHz = c.CpuClockMHz,
            HardDriveSizeGb = c.HardDriveSizeGb,
            Accounts = c.Accounts
        }).ToList();
        foreach (var console in shortConsoles)
        {
            Console.WriteLine(
                $"Short console object: CPU Clock - {console.CpuClockMHz}MHz, HDD Volume - {console.HardDriveSizeGb}, Accounts - [" +
                string.Join(", ", console.Accounts) + "]");
        }
        
        // 5
        // inner join
        Console.WriteLine("INNER JOIN:");
        // var innerJoinedConsoles = new List<string>();
        // foreach (var console in consoles)
        // {
        //     foreach (var manufacturer in manufacturers)
        //     {
        //         if (console.ManufacturerName.ToString() == manufacturer.Name)
        //         {
        //             innerJoinedConsoles.Add($"{console.Model} made by {manufacturer.Name} in {manufacturer.Country}.");
        //             break;
        //         }
        //     }
        // }
        // foreach (var consoleString in innerJoinedConsoles)
        // {
        //     Console.WriteLine(consoleString);
        // }
        var innerJoinedConsoles = consoles.Join(
            manufacturers,
            console => console.ManufacturerName.ToString(),
            manufacturer => manufacturer.Name,
            (console, manufacturer) => new
            {
                CompanyName = manufacturer.Name,
                CompanyCountry = manufacturer.Country,
                ConsoleModel = console.Model
            }
        ).ToList();
        foreach (var console in innerJoinedConsoles)
        {
            Console.WriteLine($"{console.ConsoleModel} made by {console.CompanyName} in {console.CompanyCountry}.");
        }
        
        // outer join
        Console.WriteLine("OUTER JOIN:");
        // var outerJoinedConsoles = new List<string>();
        // foreach (var console in consoles)
        // {
        //     var finded = false;
        //     
        //     foreach (var manufacturer in manufacturers)
        //     {
        //         if (console.ManufacturerName.ToString() == manufacturer.Name)
        //         {
        //             outerJoinedConsoles.Add($"{console.Model} made by {manufacturer.Name} in {manufacturer.Country}.");
        //             finded = true;
        //             break;
        //         }
        //     }
        //
        //     if (!finded)
        //     {
        //         outerJoinedConsoles.Add($"{console.Model} made by {console.ManufacturerName.ToString()} in UNKNOWN.");
        //     }
        // }
        // foreach (var consoleString in outerJoinedConsoles)
        // {
        //     Console.WriteLine(consoleString);
        // }
        var outerJoinedConsoles = from console in consoles
            join manufacturer in manufacturers on console.ManufacturerName.ToString() equals manufacturer.Name into
                JoinedManufacture
            from subManufacturer in JoinedManufacture.DefaultIfEmpty()
            select new
            {
                CompanyName = subManufacturer?.Name ?? console.ManufacturerName.ToString(),
                CompanyCountry = subManufacturer?.Country.ToString() ?? "UNKNOWN",
                ConsoleModel = console.Model
            };
        foreach (var console in outerJoinedConsoles)
        {
            Console.WriteLine($"{console.ConsoleModel} made by {console.CompanyName} in {console.CompanyCountry}.");
        }
        
        // 6
        var inputString = "В cubed голове not моей wooden опилки singing ла-ла-ла";
        Console.WriteLine(inputString);
        var outputString = inputString.RemoveLatinLetters();
        Console.WriteLine(outputString);
    }
}

