#include <math.h>

int quadraticEquation(int a, int b, int c)
{
    const int upperHalf = (-1 * b) + sqrt((b * b) - 4 * a * c);
    const int lowerHalf = 2 * a;
    return upperHalf / lowerHalf;
}