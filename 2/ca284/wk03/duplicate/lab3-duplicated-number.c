/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that finds the first number that appears twice
*/
/* include relevant libraries */
#include <stdio.h>
#include <string.h>

/* function prototypes */
void find_duplicate(char* a[], int len);

/* main function */
int main(int argc, char * argv[])
{
    find_duplicate(argv, argc);
    return 0;
}

/* actual implementation of the functions */
void find_duplicate(char* a[], int len)
{
    for (int i = 1; i < len; ++i)
    {
        for (int j = i + 1; j < len; ++j)
        {
            if (strcmp(a[i], a[j]) == 0)
            {
                printf("%s\n", a[i]);
                return;
            }
        }
    }

    printf("no duplicated number\n");
}