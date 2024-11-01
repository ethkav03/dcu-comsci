/*
Author: Ethan Kavanagh
Date: 20/10/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* function prototypes */
double sum(int*, int*);
double product(int*, int*);
double difference(int*, int*);
double division(int*, int*);
double power(int*, int*);
double logarithm(int*, int*);

/* main function */
int main(int argc, char * argv[])
{
	int c = atoi(argv[1]);                         // Initial value for a
	int d = atoi(argv[2]);
    int *a = &c;
    int *b = &d;                          // Initial value for b
	double result = 0;
    double *presult = &result;                     // Storage for results
	double (*pfunction)(int*, int*);              // Function pointer declaration

	pfunction = sum;                         // Points to function sum()
	*presult = pfunction(a, b);                // Call sum() through pointer
	printf("%.2f\n", result);

	pfunction = difference;                  // Points to function difference()
	*presult = pfunction(a, b);                // Call difference() through pointer
	printf("%.2f\n", result);

	pfunction = product;                     // Points to function product()
	*presult = pfunction(a, b);                // Call product() through pointer
	printf("%.2f\n", result);

    pfunction = division;                  // Points to function difference()
	*presult = pfunction(a, b);                // Call difference() through pointer
	printf("%.2f\n", result);

    pfunction = power;                  // Points to function difference()
	*presult = pfunction(a, b);                // Call difference() through pointer
	printf("%.2f\n", result);

    pfunction = logarithm;                  // Points to function difference()
	*presult = pfunction(a, b);                // Call difference() through pointer
	printf("%.2f\n", result);

	return 0
}

/* full implementations of functions */
double sum(int *x, int *y)
{
	return *x + *y;
}

double product(int *x, int *y)
{
	return *x * *y;
}

double difference(int *x, int *y)
{
	return *x - *y;
}

double division(int *x, int *y)
{
	return *x / *y;
}

double power(int *x, int *y)
{
    double power = pow(*x, *y);
	return power;
}

double logarithm(int *x, int *y)
{
    double xlog = log(*x);
    double ylog = log(*y);
	return xlog + ylog;
}