using System;
using System.Linq;

public static class Kata
{
    public static int[] Take(int[] arr, int n)
    {
        return arr.Take(n).ToArray();
    }
}
