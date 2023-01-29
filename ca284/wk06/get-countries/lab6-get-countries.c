/*
Author: Ethan Kavanagh
Date: 20/10/2022
Description: 
*/

/* include libraries */
#include <stdio.h>

struct Country {
    char * name;
    char * capital;
    char * population;
    char * size;
};

struct Country countries[50];

/* function prototypes */
void build_array(int n, char * a[], int *cnt);
void print_array();

/* main function */
int main(int argc, char* argv[])
{
    int count = 0;
    int *pcount = &count;

    build_array(argc, argv, pcount);

    //printf("%d\n", *pcount);

    print_array(pcount);

    return 0;
}

/* full implementations of functions */
void build_array(int n, char * a[], int *cnt)
{
    for (int i = 0; i < 50 && (i * 4 + 4) < n; ++i)
    {
        countries[i].name = a[i * 4 + 1];
        countries[i].capital = a[i * 4 + 2];
        countries[i].population = a[i * 4 + 3];
        countries[i].size = a[i * 4 + 4];
        ++(*cnt);
    }
}

void print_array(int *n)
{
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");

    for (int i = 0; i < *n; ++i)
    {
        printf("%s\t\t\t%s\t\t\t%s\t\t\t%s\n", countries[i].name, countries[i].capital, countries[i].size, countries[i].population);
    }
}