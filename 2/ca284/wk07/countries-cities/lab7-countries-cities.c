/*
Author: Ethan Kavanagh
Date: 27/10/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void build_array(int n, char * a[], int *cnt);
void sort_cities(char *names[3], int *nums);
void print_array(int *n);

struct Country {
    char * name;
    char * cities[3];
    int sizes[3];
};
struct Country countries[50];

/* main function */
int main(int argc, char* argv[])
{
    int count = 0;
    int *pcount = &count;

    build_array(argc, argv, pcount);

    for (int i = 0; i < *pcount; ++i)
    {
        sort_cities(countries[i].cities, countries[i].sizes);
    }

    print_array(pcount);

    return 0;
}

/* full implementations of functions */
void build_array(int n, char * a[], int *cnt)
{
    for (int i = 0; i < 50 && (i * 7 + 7) < n; ++i)
    {
        countries[i].name = a[i * 7 + 1];
        countries[i].cities[0] = a[i * 7 + 2];
        countries[i].sizes[0] = atoi(a[i * 7 + 3]);
        countries[i].cities[1] = a[i * 7 + 4];
        countries[i].sizes[1] = atoi(a[i * 7 + 5]);
        countries[i].cities[2] = a[i * 7 + 6];
        countries[i].sizes[2] = atoi(a[i * 7 + 7]);
        ++(*cnt);
    }
}

void sort_cities(char *names[3], int *nums)
{
    int changes;
    do
    {
        changes = 0;
        for (int i = 0; i < 2; ++i)
        {
            if (*(nums + i) < *(nums + i + 1))
            {
                char * stmp = *(names + i);
                *(names + i) = *(names + i + 1);
                *(names + i + 1) = stmp;

                int itmp = *(nums + i);
                *(nums + i) = *(nums + i + 1);
                *(nums + i + 1) = itmp;
                ++changes;
            }
        }
    }
    while (changes != 0);
}

void print_array(int *n)
{
    for (int i = 0; i < *n; ++i)
    {
        printf("%s: %s\n", countries[i].name, countries[i].cities[0]);
    }
}