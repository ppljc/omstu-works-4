namespace lab_8;

public class Building
{
    public string address;
    protected int securityCode;
    private double _vaultBalance;
    
    public string Name { get; set; }
    protected double Height { get; set; }
    private int Residents { get; set; }
    
    private static readonly Random Random = new Random();

    public Building()
    {
        Name = "Anonymous building";
        Height = 0.0;
        Residents = 0;
        address = "Unknown";
        securityCode = 1234;
        _vaultBalance = 0.0;
    }

    public Building(string name, double height, int residents, string addr, double vaultBalance)
    {
        Name = name;
        Height = height;
        Residents = residents;
        address = addr;
        securityCode = Random.Next(1000, 9999);
        _vaultBalance = vaultBalance;
    }

    protected void CheckSecurity()
    {
        Console.WriteLine($"We are checking. Current security code {securityCode}.");
    }

    private void TriggerAlarm()
    {
        Console.WriteLine($"Woop, woop, that's the sound of the police.");
    }

    public bool Demolish()
    {
        if (Height > 0.0 && Residents > 0) {
            var chance = Random.NextDouble() * 100;
            var strength = Height * 0.5;

            if (chance > strength)
            {
                Console.WriteLine($"Building {Name} was demolished.");
                
                Height = 0;
                Residents = 0;
                
                return true;
            }
            else
            {
                var diedResidents = Random.Next(0, Residents);
                
                Console.WriteLine($"Building {Name} still alive. Died {diedResidents} residents.");

                Residents -= diedResidents;
                
                return false;
            }
        }
        else
        {
            Console.WriteLine($"Building {Name} already not here.");
            
            return false;
        }
    }

    public bool Rob()
    {
        Console.WriteLine($"Trying to rob building {Name} at {address}.");
        
        TriggerAlarm();
        
        if (_vaultBalance > 0)
        {
            var chance = Random.NextDouble();

            if (chance >= 0.5)
            {
                Console.WriteLine($"Building {Name} was robbed.");

                _vaultBalance = 0;

                return true;
            }
            else
            {
                Console.WriteLine($"Building {Name} wasn't robbed.");

                return false;
            }
        }
        else
        {
            Console.WriteLine($"Building {Name} not contains any balance.");
            
            return false;
        }
    }
}