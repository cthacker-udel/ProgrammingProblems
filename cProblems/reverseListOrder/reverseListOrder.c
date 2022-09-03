#include <stdlib.h>

int *reverse_list(const int *array, size_t length)
{

    const int len = (int)length;
    int *newArray = (int *)malloc(sizeof(int) * len);
    for (int i = len - 1, j = 0; i >= 0; i--, j++)
    {
        newArray[j] = array[i];
    }
    return newArray;
}

int main(void)
{

    const int array[] = {1, 2, 3, 4};
    reverse_list(array, sizeof(int) * 4);
}
