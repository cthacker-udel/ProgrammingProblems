using System.Text.RegularExpressions;

namespace ReplaceDots;

public class ReplaceDotsClass
{
    public static string ReplaceDots(string str)
    {
        return str.Replace(".", "-");
    }

    public static void Main(string[] args) { }
}
