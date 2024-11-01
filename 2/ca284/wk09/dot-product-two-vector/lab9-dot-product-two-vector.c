/*
Author: Ethan Kavanagh
Date: 10/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void memory_exit();
void build_vector(int *pvec1, int *pstart, int *pend, char *argv[]);
void get_dot_product(int *pvec1, int *pvec2, int *pn, int *ptotal);

/* main function */
int main(int argc, char* argv[])
{
    int *pn = calloc(1, sizeof(int));
    if (!pn)
        memory_exit();
    *pn = atoi(argv[1]);

    int *pstart = calloc(1, sizeof(int));
    if (!pstart)
        memory_exit();
    *pstart = 2;

    int *pend = calloc(1, sizeof(int));
    if (!pend)
        memory_exit();
    *pend = *pn + 2;

    int *pvec1 = calloc(*pn, sizeof(int));
    if (!pvec1)
        memory_exit();
    build_vector(pvec1, pstart, pend, argv);

    *pend += *pn;

    int *pvec2 = calloc(*pn, sizeof(int));
    if (!pvec2)
        memory_exit();
    build_vector(pvec2, pstart, pend, argv);

    int *ptotal = calloc(1, sizeof(int));
    if (!ptotal)
        memory_exit();
    *ptotal = 0;

    free(pstart);
    free(pend);

    get_dot_product(pvec1, pvec2, pn, ptotal);

    free(pn);
    free(pvec2);
    free(pvec1);

    printf("%d\n", *ptotal);

    free(ptotal);

    return 0;
}

/* full implementations of functions */
void memory_exit()
{
    printf("Failed to allocate memory.");
    exit(0);
}

void build_vector(int *pvec1, int *pstart, int *pend, char *argv[])
{
    for (int i = *pstart; i < *pend; ++i)
    {
        //printf("%d\n", i);
        *(pvec1 + i - *pstart) = atoi(*(argv + i));
    }
    *pstart = *pend;
}

void get_dot_product(int *pvec1, int *pvec2, int *pn, int *ptotal)
{
    for (int i = 0; i < *pn; ++i)
    {
        *ptotal += *(pvec1 + i) * *(pvec2 + i);
    }
}