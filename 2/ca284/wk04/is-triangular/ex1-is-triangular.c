/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Determines whether a number is triangular or not
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* function prototypes */
bool is_triangular(int n);

/* main function */
int main(int argc, char* argv[])
{
    int n = atoi(argv[1]); // converts argument to integer

    if (is_triangular(n)) // prints result based on value returned by is_triangular function
        printf("%d is a triangular number\n", n);
    else
        printf("%d is not a triangular number\n", n);

    return 0;
}

/* full implementations of functions */

/* function determines if number is triangular */
bool is_triangular(int n)
{
    int m = 0;
    int len = 1;
    for (int i = 1; m < n; ++i) // builds the triangular numbers array
    {
        m = i * (i + 1) / 2; // triangular number formula
        if (m == n) // checks if n is a triangular number
            return true;
    }
    return false;
}