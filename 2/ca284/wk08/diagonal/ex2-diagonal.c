/*
Author: Ethan Kavanagh
Date: 03/11/2022
Description: Finds the sum of the anti-diagonal of a 2D matrix.
    Reads the command line arguments into a 2D matrix.
    Adds up and prints the sum of the anti-diagonal.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void build_matrix(int *pm, int n, int len, char * a[]);
void calculate_result(int *pm, int n, int *total);

/* main function */
int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);                  //initializes the size of the matrix

    int matrix[n][n];                       //initializes a blank 2D matrix
    int *pm = &matrix[0][0];                //creates a pointer to matrix

    build_matrix(pm, n, argc - 2, argv);    //calls function to populate 2D matrix

    int result = 0;                         //initializes variable to store result
    int *presult = &result;                 //creates pointer to result

    calculate_result(pm, n, presult);       //calls function to calculate the anti-diagonal

    printf("%d\n", *presult);               //prints the anti-diagonal

    return 0;
}

/* full implementations of functions */
void build_matrix(int *pm, int n, int len, char * a[])
{
    for (int i = 0; i < n * n; ++i)             //loops through the argv
    {
        *(pm + i) = atoi(*(a + i + 2));         //populates the 2D matrix using values of argv
    }
}

void calculate_result(int *pm, int n, int *total)
{
    for (int i = 1; i < n + 1; ++i)             //loops through 2D matrix
    {
        *total += *(pm + (n * i) - i);          //adds up the total and sets its value to result
    }
}