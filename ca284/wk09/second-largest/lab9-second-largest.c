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
void build_array(float *nums, int len, char *args[]);
void sort_array(float *nums, int len);
void swap(float *a, float *b);
void find_second_biggest(float * nums, int len, float *secbig);

/* main function */
int main(int argc, char* argv[])
{
    float *nums = calloc(argc - 1, sizeof(float));
    if (!nums)
        memory_exit();

    build_array(nums, argc - 1, argv);

    sort_array(nums, argc - 1);

    float *second_largest = calloc(1, sizeof(float));
    if (!second_largest)
        memory_exit();

    find_second_biggest(nums, argc - 1, second_largest);
    free(nums);

    printf("%.1f\n", *second_largest);
    free(second_largest);

    return 0;
}

/* full implementations of functions */
void memory_exit()
{
    printf("Failed to allocate memory.");
    exit(0);
}

void build_array(float *nums, int len, char *args[])
{
    for (int i = 0; i < len; ++i)
    {
        *(nums + i) = atof(*(args + i + 1));
    }
}

void sort_array(float *nums, int len)
{
    int changes;
    do
    {
        changes = 0;
        for (int i = 0; i < len - 1; ++i)
        {
            if (*(nums + i) < *(nums + i + 1))
            {
                swap(nums + i, nums + i + 1);
                ++changes;
            }
        }
    }
    while (changes > 0);
}

void swap(float *a, float *b)
{
    int tmp = *a;                   //assigns temporary variable to address of a
    *a = *b;                        //assigns value at address of a to value at address of b
    *b = tmp;                       //assigns value at address of b to value of twmporary variable
}

void find_second_biggest(float * nums, int len, float *secbig)
{
    int biggest = *nums;
    for (int i = 0; i < len; ++i)
    {
        //printf("%f\n", *(nums + i));
        if (*(nums + i) < biggest)
        {
            *secbig = *(nums + i);
            return;
        }
    }
}