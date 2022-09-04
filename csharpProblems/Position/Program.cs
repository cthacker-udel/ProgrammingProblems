public class Kata
{
    public static string Position(char alphabet)
    {
        string lower = "abcdefghijklmnopqrstuvwxyz";
        return lower.IndexOf(alphabet.ToString().ToLower()) + 1;
    }
}
