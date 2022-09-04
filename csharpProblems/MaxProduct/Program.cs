using System.Linq;
using System;
using System.Collections.Generic;

public class Kata
{
    public static int MaxProduct(int[] arr, int size)
    {
        List<int> sorted = arr.ToList();
        sorted.Sort();
        sorted.Reverse();
        return sorted.Take(size).Aggregate((e1, e2) => e1 * e2);
    }
}