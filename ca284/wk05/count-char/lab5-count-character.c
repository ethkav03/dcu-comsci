/*
Author: Ethan Kavanagh
Date: 13/10/2022
Description: Program
*/

/* include libraries */
#include <stdio.h>
#include <string.h>

/* function prototypes */
int count_char(char *c, char *s);

/* main function */
int main(int argc, char* argv[])
{
    int count = 0;
    int *pcount = &count;
    char chr = argv[1][0];
    char *pchr = &chr;
    char *str = argv[2];

    *(pcount) = count_char(*pchr, str);

    printf("%i\n", count);

    return 0;
}

/* full implementations of functions */
int count_char(char *c, char *s)
{
    int counter = 0;
    for (int i = 0; s[i] != '\0'; ++i)
    {
        if (*(s + i) == *(c))
        {
            ++counter;
        }
    }
    return counter;
}