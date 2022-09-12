public class Kata
{
    public static int Position(char alphabet)
    {
        string lower = "abcdefghijklmnopqrstuvwxyz";
        return lower.IndexOf(alphabet.ToString().ToLower()) + 1;
    }
}
