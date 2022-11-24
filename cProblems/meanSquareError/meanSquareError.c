#include <stddef.h>

double mean_square_error(size_t n, const int a[n], const int b[n])
{
    double absSum = 0;
    for (int i = 0; i < n; i++)
    {
        int diff = abs(a[i] - b[i]);
        absSum += diff * diff;
    }
    return absSum / n;
}