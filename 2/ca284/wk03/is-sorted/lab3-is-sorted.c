/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that sorts the numbers in increasing order
*/
/* include relevant libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void sortArray(int a[], int len);
void printArray(int b[], int len);

/* main function */
int main(int argc, char * argv[])
{
    int a[argc - 1];
    for (int i = 0; i < argc - 1; ++i)
    {
        a[i] = atoi(argv[i + 1]);
    }
    sortArray(a, argc);

    printArray(a, argc);
    return 0;
}

/* actual implementation of the functions */
/* sorts the numbers into increasing order */
void sortArray(int a[], int len)
{
    int changes;
    do
    {
        changes = 0;
        for (int i = 0; i < len - 2; ++i)
        {
            if (a[i] > a[i + 1])
            {
                int tmp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = tmp;
                ++changes;
            }
        }
    }
    while (changes > 0);
}

/* prints the numbers in the array */
void printArray(int b[], int len)
{
    for (int i = 0; i < len - 1; ++i)
    {
        printf("%d\n", b[i]);
    }
}