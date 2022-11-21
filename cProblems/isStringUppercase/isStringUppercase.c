#include <ctype.h>
#include <stdbool.h>

bool is_uppercase(const char *source)
{
    int i = 0;
    while (source[i] != '\0')
    {
        if (!isupper(source[i]) && isalpha(source[i]))
        {
            return false;
        }
        i++;
    }
    return true;
}