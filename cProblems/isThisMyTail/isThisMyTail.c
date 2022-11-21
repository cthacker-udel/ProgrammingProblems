#include <string.h>

int correct_tail(const char *body, const char *tail)
{
    return body[strlen(body) - 1] == tail[0];
}