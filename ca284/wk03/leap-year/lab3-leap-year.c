/*
    Author: Ethan Kavanagh
    Date: 03/10/2022
    Description: Program that finds longest word in sentence
*/
/* include relevant libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void print_years(int start, int end);

/* main function */
int main(int argc, char * argv[])
{
    int start = atoi(argv[1]);
    int end = atoi(argv[2]);

    print_years(start, end);
    
    return 0;
}

/* actual implementation of the functions */
void print_years(int start, int end)
{
    for (int i = start; i <= end; ++i)
    {
        if (i % 100 == 0)
        {
            if (i % 400 == 0)
            {
                printf("%d\n", i);
            }
            else
            {
                ++i;
            }
        }
        else if (i % 4 == 0)
        {
            printf("%d\n", i);
        }
    }
}