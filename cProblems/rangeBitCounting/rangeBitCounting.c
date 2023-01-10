#include <stdlib.h>
#include <stdio.h>
typedef unsigned int ui;

ui range_bit_count(ui a, ui b)
{
    int totalCount = 0;
    for (int i = a; i <= b; i++)
    {
        int count = 0;
        int _i = i;
        while (_i > 0)
        {
            count += _i % 2;
            _i /= 2;
        }
        totalCount += count;
    }
    return totalCount;
}

int main(void)
{
    printf("%d\n", range_bit_count(2, 7));
}