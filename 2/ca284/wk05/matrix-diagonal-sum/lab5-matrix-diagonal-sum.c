/*
Author: Ethan Kavanagh
Date: 14/10/2022
Description: Calculates the sum of the n x n matrix
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void construct_matrix(int *mtrx, int len, char *args[]);
void calculate(int *m, int *a, int *len);

/* main function */
int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);
    int *pn = &n;

    int matrix[*pn][*pn];
    int *pmatrix = &matrix[0][0];

    int diagonal = 0;
    int *pdiagonal = &diagonal;

    construct_matrix(pmatrix, argc, argv);
    calculate(pdiagonal, pmatrix, pn);

    printf("%d\n", *pdiagonal);
    return 0;
}

/* full implementations of functions */
void construct_matrix(int *mtrx, int len, char *args[])
{
    for (int i = 2; i < len; ++i)
    {
        *(mtrx + i - 2) = atoi(*(args + i));
    }
}

void calculate(int *m, int *a, int *len)
{
    for (int i = 0; i < *len; ++i)
    {
        *m += *(a + (i + (*len * i)));
    }
}