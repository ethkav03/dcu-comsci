/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Program that finds the largest or smallest number depending on which is specified by user
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* function prototypes */
float find_largest(int len, float a[]);
float find_smallest(int len, float a[]);

/* main function */
int main(int argc, char* argv[])
{
    char* requirement = argv[1];
    float n;

    float a[50];
    for (int i = 0; i < argc - 2; ++i) // builds array of numbers
    {
        a[i] = atof(argv[i + 2]);
    }

    if (strcmp(requirement, "largest") == 0) // checks if user specified largest or smallest number
    {
        n = find_largest(argc -2, a);
    }
    else if (strcmp(requirement, "smallest") == 0)
    {
        n = find_smallest(argc - 2, a);
    }

    printf("%.2f\n", n);

    return 0;
}

/* full implementations of functions */

/* finds largest number */
float find_largest(int len, float a[])
{
    float largest = 0;
    for (int i = 0; i < len; ++i) // searches for the largest number
    {
        if (a[i] > largest)
        {
            largest = a[i];
        }
    }
    return largest;
}

/* finds smallest number */
float find_smallest(int len, float a[])
{
    float smallest = a[0];
    for (int i = 1; i < len; ++i) // searches for the smallest number
    {
        if (a[i] < smallest)
        {
            smallest = a[i];
        }
    }
    return smallest;
}