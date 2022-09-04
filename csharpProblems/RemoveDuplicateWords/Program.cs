using System.Linq;

namespace RemoveDuplicateWordsNamespace;

public class RemovingWordsClass
{
    public static string RemoveDuplicateWords(string s)
    {
        return string.Join(" ", s.Split(" ").Distinct());
    }
}
