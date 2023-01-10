#include <stddef.h>
#include <limits.h>
#include <stdio.h>

int find_max_product(size_t length, const int array[length])
{
    int max_product = INT_MIN;
    for (int i = 0; i < length; i++)
    {
        // the # of digits apart
        int total_product = 1;
        for (int j = i; j < length; j += i + 1)
        {
            total_product *= array[j];
        }
        max_product = total_product > max_product ? total_product : max_product;
    }
    return max_product;
}

int main(void)
{
    int arr[7] = {11, 6, -2, 0, 5, -4, 2};
    printf("%d\n", find_max_product(sizeof(int) * 7, arr));
}