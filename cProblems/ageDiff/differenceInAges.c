#include <stdlib.h>
#include <limits.h>

#define MIN(x, y) x < y ? x : y
#define MAX(x, y) x > y ? x : y

int *difference_in_ages(size_t a, const int ages[a])
{
    int minAge = INT_MAX;
    int maxAge = INT_MIN;
    for (int i = 0; i < (int)a; i++)
    {
        minAge = MIN(ages[i], minAge);
        maxAge = MAX(ages[i], maxAge);
    }
    int *arr = malloc(sizeof(int) * 3);
    arr[0] = minAge;
    arr[1] = maxAge;
    arr[2] = maxAge - minAge;
    return arr;
}