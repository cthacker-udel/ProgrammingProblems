using System;

public static class Kata
{
    public static int WordsToMarks(string str)
    {
        string lower = "abcdefghijklmnopqrstuvwxyz";
        int sum = str.ToLower().ToCharArray().Select(e => lower.IndexOf(e) + 1).Sum();
        return sum;
    }
}