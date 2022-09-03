#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>

int numberLength(int num)
{
    int len = 1;
    while (num >= 10)
    {
        num /= 10;
        len++;
    }
    return len;
}

bool validateSection(const char *section)
{

    if (strlen(section) < 2)
    {
        if (strlen(section) == 0)
        {
            return false;
        }
        else
        {
            return isdigit(section[0]);
        }
    }
    else
    {
        const int parsed = atoi(section);
        const int parsedLength = numberLength(parsed);
        return parsedLength == strlen(section) && strlen(section) <= 3 && parsed <= 255;
    }
}

bool is_valid_ip(const char *addr)
{
    char *addrPtr = (char *)malloc(sizeof(char) * strlen(addr) + 1);
    strcpy(addrPtr, addr);
    int octetCount = 0;
    char *token;
    const char s[2] = ".";
    token = strtok(addrPtr, s);
    while (token != NULL)
    {
        if (!validateSection(token))
        {
            return false;
        }
        octetCount++;
        token = strtok(NULL, s);
    }
    return octetCount == 4;
}

int main(void)
{
    is_valid_ip(".1.45.227");
}