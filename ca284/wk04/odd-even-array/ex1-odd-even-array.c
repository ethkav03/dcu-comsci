/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Adds the odds numbers. Then subtracts the 2nd onwards even numbers from the 1st even number.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
int add_odds(int len, int a[]);
int find_difference(int len, int b[]);

/* main function */
int main(int argc, char* argv[])
{
    int sum, difference;

    int a[50];
    int len = argc - 1;
    for (int i = 0; i < len; ++i) // cunstructs the array of numbers
    {
        a[i] = atoi(argv[i + 1]);
    }

    sum = add_odds(len, a);
    printf("%d\n", sum);

    difference = find_difference(len, a);
    printf("%d\n", difference);

    return 0;
}

/* full implementations of functions */

/* sums all the odd numbers together */
int add_odds(int len, int a[])
{
    int sum = 0;
    for (int i = 0; i < len; ++i)
    {
        if (a[i] % 2 == 1) // checks for odd number
        {
            sum += a[i]; // increases sum by a[i]
        }
    }
    return sum;
}

/* finds 1st even number and then subtracts all the remaining even numbers */
int find_difference(int len, int b[])
{
    int diff = 0;
    int first = 0;

    for (int i = 0; i < len; ++i) // checks for the first even number
    {
        if (b[i] % 2 == 0) 
        {
            diff = b[i];
            first = b[i];
            break;
        }
    }
    //printf("%d\n", first);

    for (int i = 0; i < len; ++i) //subtracts the remaining even numbers from the first one
    {
        if (b[i] % 2 == 0) 
        {
            diff -= b[i];
        }
        //printf("%d %d\n", b[i], diff);
    }

    return diff + first;
}