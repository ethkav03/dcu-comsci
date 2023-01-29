/*
Author: Ethan Kavanagh
Date: 14/10/2022
Description: Searches for a substring inside of a string
*/

/* include libraries */
#include <stdio.h>
#include <string.h>

/* function prototypes */
void find_index(char *str, char *sub, int *indx, int slen, int sublen);

/* main function */
int main(int argc, char* argv[])
{
    char *string = argv[1];
    char *substring = argv[2];
    
    int index = 0;
    int *pindex = &index;

    find_index(string, substring, pindex, strlen(string), strlen(substring));

    printf("%d %ld\n", *pindex, *pindex + strlen(substring) - 1);

    return 0;
}

/* full implementations of functions */
void find_index(char *str, char *sub, int *indx, int slen, int sublen)
{
    char *start = strstr(str, sub);

    for (int i = 0; i < slen; ++i)
    {
        if (*(str + i) == *start)
        {
            *indx = i;
        }
    }
}