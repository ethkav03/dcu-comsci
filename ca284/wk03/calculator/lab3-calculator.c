/*
Author: Ethan Kavanagh
Date: 29/09/2022
Description: Program that makes a divide or multiply calculation
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* function prototypes */
float calculate(char type[], float n1, float n2);

/* main function */
int main(int argc, char* argv[])
{
    if (argc < 4)
    {
        printf("Too few arguments.\n");
        return 1;
    }
    if (argc > 4)
    {
        printf("Too many arguments.\n");
        return 1;
    }
    if (strcmp(argv[1], "multiply") != 0 && strcmp(argv[1], "divide") != 0)
    {
        printf("Function accepts only 'divide' or 'multiply' arithmetic\n");
        return 1;
    }

    float num1 = atof(argv[2]);
    float num2 = atof(argv[3]);

    if (strcmp(argv[1], "divide") == 0 && num2 == 0)
    {
        printf("invalid\n");
        return 0;
    }

    float result = calculate(argv[1], num1, num2);

    printf("%.6f\n", result);

    return 0;
}

/* calculation function */
float calculate(char type[], float n1, float n2)
{
    if (strcmp(type, "divide") == 0)
        return n1 / n2;
    else
        return n1 * n2;
}