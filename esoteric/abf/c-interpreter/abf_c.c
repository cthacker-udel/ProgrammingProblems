#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int numLength(int num)
{
    int len = 1;
    while (num >= 10)
    {
        num /= 10;
        len++;
    }
    return len;
}

void parseTape(char *origTape)
{
    char *tape = (char *)malloc(sizeof(char) * strlen(origTape) + 1);
    strcpy(tape, origTape);
    int accumulator = 0;
    int index = 0;
    int bIndex = 0;
    char *output = (char *)malloc(sizeof(char) * 1);
    while (index < strlen(tape))
    {
        char command = tape[index];
        switch (command)
        {
        case '!':
        {
            index++;
            break;
        }
        case 'a':
        {
            const int accumulatorLength = numLength(accumulator) + 1;
            char tempNumber[accumulatorLength];
            itoa(accumulator, tempNumber, 10);
            realloc(output, sizeof(char) * (strlen(output) + accumulatorLength));
            strcat(output, tempNumber);
            break;
        }
        case 'B':
        {
            int startingIndex = index;
            do
            {
                startingIndex++;
                if (tape[startingIndex] == 'B')
                {
                    bIndex = startingIndex;
                    break;
                }
            } while (startingIndex < strlen(tape));
            int diff = startingIndex - index;
            realloc(tape, (sizeof(char) * strlen(tape) + diff + 1));
            char *chunk = (char *)malloc(sizeof(char) * diff + 1);
            for (int i = index; i <= startingIndex; i++)
            {
                chunk[i] = tape[i];
            }
            strcat(tape, chunk);
            break;
        }
        case 'F':
        {
            accumulator += 5;
            break;
        }
        case '\'':
        {
            break;
        }
        }
        index++;
    }
    printf("%s", output);
}

int main(void)
{
    parseTape("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFa");
}