/*
Author: Ethan Kavanagh
Date: 13/10/2022
Description: Finds the most common occuring character.
*/

/* include libraries */
#include <stdio.h>

/* function prototypes */
void count_letters(char *s, int *a);
char find_max(int *a);

/* main function */
int main(int argc, char* argv[])
{
    char most_commmon;

    char *pstring = argv[1];
    int counts[57] = {0};
    int *pcounts = &counts[0];

    count_letters(pstring, pcounts);

    most_commmon = find_max(pcounts);
    printf("%c\n", most_commmon);
}

/* full implementations of functions */
void count_letters(char *s, int *a)
{
    for (int i = 0; *(s + i) != '\0'; ++i)
    {
        ++(*(a + (*(s + i) - 65)));
    }
}
char find_max(int *a)
{
    int max = 0;
    for (int i = 0; i < 57; ++i)
    {
        if (*(a + i) > *(a + max))
        {
            max = i;
        }
    }
    return (char)(max + 65);
}