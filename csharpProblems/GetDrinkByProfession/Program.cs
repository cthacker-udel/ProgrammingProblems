using System;
using System.Collections.Generic;

public class Kata
{
    public static string GetDrinkByProfession(string p)
    {
        Dictionary<string, string> drinks = new Dictionary<string, string>
        {
            { "Jabroni", "Patron Tequila" },
            { "School Counselor", "Anything with Alcohol" },
            { "Programmer", "Hipster Craft Beer" },
            { "Bike Gang Member", "Moonshine" },
            { "Politician", "Your tax dollars" },
            { "Rapper", "Cristal" }
        };

        return drinks.ContainsKey(p.ToLower()) ? drinks[p] : "Beer":
    }
}
