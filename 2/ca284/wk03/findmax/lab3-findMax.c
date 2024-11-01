/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that finds the biggest number in the list
*/
/* include relevant libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
int findMax(char * a[], int len);

/* main function */
int main(int argc, char * argv[])
{
	int max = findMax(argv, argc);

    printf("%d\n", max);
	return 0;
}

/* actual implementation of the functions */
int findMax(char * a[], int len)
{
    int max = 0;

    for (int i = 0; i < len; ++i)
    {
        if (atoi(a[i]) > max)
        {
            max = atoi(a[i]);
        }
    }

    return max;
}