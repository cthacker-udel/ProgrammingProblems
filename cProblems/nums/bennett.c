#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void paceCar()
{
    char *flag = malloc(28 * sizeof(char));
    int arr[28] = {110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125};
    int arrLength = 28;

    for (int i = 0; i < arrLength; i++)
    {

        if (arr[i] <= 10)
        {
            continue;
        }
        int *value = arr + i;
        char *cast = (char *)value;
        strcat(flag, cast);
    }
    puts(flag);
}

int main()
{
    paceCar();
}