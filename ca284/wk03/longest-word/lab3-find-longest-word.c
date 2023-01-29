/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that finds longest word in sentence
*/
/* include relevant libraries */
#include <stdio.h>
#include <string.h>

/* function prototypes */
void longest(char sentence[]);

/* main function */
int main(int argc, char * argv[])
{
    longest(argv[1]);
    
    return 0;
}

/* actual implementation of the functions */
void longest(char sentence[])
{
    int start = 0;
    int end = 0;
    int wordLen = 0;
    int j = 0;
    int len = strlen(sentence);

    for (int i = 0; i < len + 1; ++i)
    {
        if (sentence[i] == ' ' || sentence[i] == '\0')
        {
            if (i - j > wordLen)
            {
                end = i;
                start = j;
                wordLen = end - j;
            }
            j = i + 1;
        }
    }
    for (int i = start; i < end; ++i)
    {
        printf("%c", sentence[i]);
    }
    printf("\n");
}