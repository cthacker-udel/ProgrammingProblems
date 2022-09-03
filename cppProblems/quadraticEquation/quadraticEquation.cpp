#include <cmath>
#include <iostream>

/**
 * Function for generating the resultant of the quadratic equation given a, b, and c
 *
 * @param a - A in the quadratic equation
 * @param b - B in the quadratic equation
 * @param c - C in the quadratic equation
 *
 * @returns The resultant of the quadratic equation given a, b, and c
 *
 */
int quadraticEquation(int a, int b, int c)
{

    const int upperHalf = (-1 * b) + sqrt((b * b) - 4 * a * c);
    std::cout << "UpperHalf = " << upperHalf << std::endl;
    const int lowerHalf = 2 * c;
    return upperHalf / lowerHalf;
}