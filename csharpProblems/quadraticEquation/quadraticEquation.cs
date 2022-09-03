using System;

namespace QuadraticEquation;


/// <summary>
/// Calculates the root of the quadratic equation given a, b, and c
/// </summary>
/// <param name="a">A in the quadratic equation</param>
/// <param name="b">B in the quadratic equation</param>
/// <param name="c">C in the quadratic equation</param>
/// <returns>Returns the resultant of the quadratic equation given a, b, and c</returns>
public static int quadraticEquation(int a, int b, int c)
{

    const int upperHalf = (-1 * b) + System.Math.Sqrt((b * b) - 4 * a * c);
    const int lowerHalf = 2 * a;
    return upperHalf / lowerHalf;

}