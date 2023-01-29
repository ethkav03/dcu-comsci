/*
Author: Ethan Kavanagh
Date: 25/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/* function prototypes */
void build_binary(int *binary, int argc, char *args[], int *len);
void check(char *s);
void bin_to_dec(int len, int *binary, int *total);

/* main function */
int main(int argc, char* argv[])
{
    if (argc > 9)
    {
        printf("Too many binary digits entered.\n");
        exit(0);
    }

    int *binary = calloc(argc - 1, sizeof(int));
    int *len = malloc(sizeof(int));
    build_binary(binary, argc, argv, len);

    int *total = malloc(sizeof(int));
    bin_to_dec(argc - 1, binary, total);

    printf("%d\n", *total);

    return 0;
}

/* full implementations of functions */
void build_binary(int *binary, int argc, char *args[], int *len)
{
    for (int i = 0; i < argc - 1; ++i)
    {
        check(*(args + i + 1));
        *(binary + i) = atoi(*(args + i + 1));
        ++(*len);
    }
}

void check(char *s)
{
    if (strcmp(s, "1") != 0 && strcmp(s, "0") != 0)
    {
        printf("Only digits 1 and 0 are permitted.\n");
        exit(0);
    }
}

void bin_to_dec(int len, int *binary, int *total)
{
    for (int i = 0; i < len; ++i)
    {
        *total += *(binary + i) * pow(2, (len - i - 1));
    }
}