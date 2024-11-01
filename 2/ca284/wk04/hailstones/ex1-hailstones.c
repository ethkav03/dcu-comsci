/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Takes in an integer and outputs the following hailstone sequence numbers until it reaches 1
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
int hailstone(int n);

/* main function */
int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);

    int h = hailstone(n);

    printf("%d\n", h);

    return 0;
}

/* full implementations of functions */

/* recursive function that calculates the hailstone sequence */
int hailstone(int n)
{
    if (n == 1)
        return 1;

    printf("%d ", n);

    if (n % 2 == 0) // runs hailstone calculation
        return hailstone(n / 2);
    else
        return hailstone(3 * n + 1);
}