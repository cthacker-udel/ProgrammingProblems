#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char **inArray(char *array1[], int sz1, char *array2[], int sz2, int *lg)
{
    char **sortedArray = (char **)malloc(sizeof(char *) * sz1 + 1);
    int *indexes = (int *)malloc(sizeof(int) * 1);
    int ind = 0;
    for (int i = 0; i < sz1; i++)
    {
        char *theStr = array1[i];
        for (int j = 0; j < sz2; j++)
        {
            if (strstr(array2[j], theStr))
            {
                sortedArray[ind] = (char *)malloc(sizeof(char) * strlen(theStr) + 1);
                strcpy(sortedArray[ind], theStr);
                for (int i = 0; i < ind - 1; i++)
                {
                    if (strcmp(sortedArray[ind], sortedArray[ind + 1]) > 0)
                    {
                        char *word1 = sortedArray[ind];
                        char *word2 = sortedArray[ind + 1];
                        sortedArray[ind + 1] = word1;
                        sortedArray[ind] = word2;
                    }
                }
                array2[j] = "";
                break;
            }
        }
    }
    *lg = ind;
    return sortedArray;
}

int main(void)
{
    char *arr1[3] = {"arp", "live", "strong"};
    char *arr2[5] = {"lively", "alive", "harp", "sharp", "armstrong"};
    int lg;
    inArray(arr1, 3, arr2, 5, &lg);
}