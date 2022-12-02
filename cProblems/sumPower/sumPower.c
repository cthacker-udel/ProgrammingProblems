#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdio.h>

unsigned long long sumDig(int n)
{
    char *strNum;
    strNum = itoa(n, strNum, 10);
    int total = 0;
    for (int i = 0; i < strlen(strNum); i++)
    {
        total += strNum[i] - '0';
    }
    return total;
}

unsigned long long power_sum_dig_term(unsigned n)
{
    int *collector_arr = malloc(sizeof(int) * 1);
    int collector_len = 1;
    collector_arr[0] = 81;
    int power = 3;
    int starter = 9;
    int curr_num = 81;
    int power_limit = 6;
    printf("Before while\n");
    while (collector_len < n)
    {
        for (int i = 2;; i++)
        {
            for (int j = 2;; j++)
            {
                unsigned long long pow_num = (unsigned long long)pow(i, j);
                if (pow_num % i == 0 && sumDig(pow_num) == i && log(pow_num) / log(i) == j && pow_num > curr_num)
                {
                    printf("in if\n");
                    collector_arr = (int *)realloc(collector_arr, sizeof(int) * (collector_len + 1));
                    collector_arr[collector_len - 1] = pow_num;
                }
            }
        }
    }
    printf("Result = %d\n", collector_arr[collector_len - 1]);
    return collector_arr[collector_len - 1];
}

// 2  -- 9   | 9 * 9          | 81
// 3  -- 8   | 8 * 8 * 8      | 512
// 4  -- 7   | 7 * 7 * 7 * 7  | 2401
// 3  -- 17  | 17 * 17 * 17   | 4913
// 3  -- 18  | 18 * 18 * 18   | 5832
// 3  -- 26  | 26 * 26 * 26   | 17576

int main(void)
{
    printf("Result = %d\n", power_sum_dig_term(2));
}