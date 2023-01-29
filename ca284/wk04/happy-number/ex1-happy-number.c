/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Determines whether a number is a happy number or not.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* function prototypes */
int is_happy(int n);
int calculations(int m);

/* main function */
int main(int argc, char* argv[])
{
    const int n = atoi(argv[1]);

    int result = is_happy(n);

    if (result == 1) // prints the output based on the result
        printf("is happy\n");
    else
        printf("not happy\n");

    return 0;
}

/* full implementations of functions */

/* function that determines if a number is happy or not */
int is_happy(int n)
{
    int history[n];
    
    int len = 0;

    for (int i = 0; i < n; ++i)
    {
        int total = calculations(n);
        n = total; // sets n to the current total

        if (total == 1) //returns 1 if total is 1
        {
            return 1;
        }
        else
        {
            for (int j = 0; j < len; ++j) // loops through history of totals
            {
                if (history[j] == total) // if total has been that value before it returns 0 (0 stands for false)
                {
                    return 0;
                }
            }
            history[i] = total; // otherwise adds the total to the array
            ++len;
        }
    }
}

/* function that performs the calculation on the number */
int calculations(int m)
{
    int total = 0;
    while(m > 0) // performs the calculation on the number m
    {
        total += (m % 10) * (m % 10); // squares the digit
        m = m / 10; // removes digit from number
    }
    return total;
}