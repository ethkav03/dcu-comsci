/*
Author: Ethan Kavanagh
Date: 10/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void exit_program();
void build_array(int *nums, int len, char *argc[]);
void sort_array(int *nums, int len);
void swaps(int *a, int *b);
void find_twice(int *nums, int len, int *number);

/* main function */
int main(int argc, char* argv[])
{
    int *nums = calloc(argc - 1, sizeof(int));
    if (!nums)
        exit_program();

    build_array(nums, argc - 1, argv);

    sort_array(nums, argc - 1);

    int *twice = calloc(1, sizeof(int));
    if (!twice)
        exit_program();

    find_twice(nums, argc - 1, twice);
    free(nums);

    printf("%d\n", *twice);
    free(twice);

    return 0;
}

/* full implementations of functions */
void exit_program()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

void build_array(int *nums, int len, char *argc[])
{
    for (int i = 0; i < len; ++i)
    {
        *(nums + i) = atoi(*(argc + i + 1));
    }
}

void sort_array(int *nums, int len)
{
    int changes;
    do
    {
        changes = 0;
        for (int i = 0; i < len; ++i)
        {
            if (*(nums + i) < *(nums + i + 1))
            {
                swaps(nums + i, nums + i + 1);
                ++changes;
            }
        }
    } 
    while (changes > 0);
}

void swaps(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void find_twice(int *nums, int len, int *number)
{
    for (int i = 0; i < len; ++i)
    {
        for (int j = i + 1; j < len; ++j)
        {
            if (*(nums + i) % *(nums + j) == 0)
            {
                *number = *(nums + i);
                return;
            }
        }
    }
}