#include <stdlib.h>
#include <stdio.h>
typedef unsigned long long ull;

ull even_fib(ull limit)
{
    ull *fib = (ull *)malloc(sizeof(ull) * 3);
    ull *evens = (ull *)malloc(sizeof(ull) * 1);
    fib[0] = 0;
    fib[1] = 1;
    fib[2] = 1;
    evens[0] = 0;
    int len = 3;
    int ind = 2;
    int evenIndex = 0;
    ull new_number = 0;
    while (new_number < limit)
    {
        len++;
        fib = (ull *)realloc(fib, sizeof(ull) * len);
        ind++;
        new_number = fib[ind - 1] + fib[ind - 2];
        fib[ind] = new_number;
        if (new_number % 2 == 0 && new_number < limit)
        {
            evenIndex++;
            evens = (ull *)realloc(evens, sizeof(ull) * (evenIndex + 1));
            evens[evenIndex] = new_number;
        }
    }
    ull sum = 0;
    for (int i = 0; i < evenIndex + 1; i++)
    {
        sum += evens[i];
    }
    return sum;
}

int main(void)
{
    printf("Result = %u\n", even_fib(10));
}