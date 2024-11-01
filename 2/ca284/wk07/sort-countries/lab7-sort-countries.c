/*
Author: Ethan Kavanagh
Date: 27/10/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

struct Country {
    char * name;
    char * capital;
    char * population;
    char * size;
};

struct Country countries[50];
const int MAX = 100000;

/* function prototypes */
void build_array(int n, char * a[], int *cnt);
void sort_array(int * n);
void print_array(int * n);

/* main function */
int main(int argc, char* argv[])
{
    int count = 0;
    int *pcount = &count;

    build_array(argc, argv, pcount);

    sort_array(pcount);

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

void sort_array(int *n)
{
    int changes;
    do
    {
        changes = 0;
        for (int i = 0; i < *n - 1; ++i)
        {
            if (atoi(countries[i].population) < atoi(countries[i + 1].population))
            {
                struct Country tmp = countries[i];
                countries[i] = countries[i + 1];
                countries[i + 1] = tmp;
                ++changes;
            }
        }
    }
    while (changes != 0);
}

void print_array(int *n)
{
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");

    for (int i = 0; i < *n; ++i)
    {
        printf("%s\t\t\t%s\t\t\t%s\t\t\t%s\n", countries[i].name, countries[i].capital, countries[i].size, countries[i].population);
    }
}