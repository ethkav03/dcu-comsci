/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that locates the specified number
*/
/* include relevant libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* function prototypes */
int search(char* a[], int len, char key[]);

/* main function */
int main(int argc, char * argv[])
{
    int index = search(argv, argc, argv[1]);
	
    printf("Found %s at %d\n", argv[1], index);
	return 0;
}

/* actual implementation of the functions */
int search(char* a[], int len, char key[])
{
    for (int i = 2; i < len; ++i)
    {
        if (strcmp(a[i], key) == 0)
        {
            return i - 2;
        }
    }
}