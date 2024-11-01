/*
Author: Ethan Kavanagh
Date: 30/11/2022
Description: Finds all the frequent numbers (all number that occur more than three times) and then prints them all out
Approach: Read all number into an array. Sort the array in ascending order. Creates a list of Numbers (a creates struct). Checks if
    if number in list is in a struct already. If it is it increments the structs count. If not it reallocates memory and creates a new Number
    struct. Finds all structs which occur atleast 3 times. Prints all frequent numbers.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct {
    int number;
    int count;
} Number;

/* function prototypes */
void build_array(int *n, char* argv[], int len, int *cap);
void sort_array(int *nums, int len);
void swap(int *a, int *b);
void count_numbers(Number *numbers, int *nums, int len, int *num_len);
Number create_num(int n);
void find_frequent(int *freq, int *freq_len, Number *numbers, int *num_len);
void print_frequents(int *freq, int *freq_len, Number *numbers, int *num_len);

/* main function */
int main(int argc, char* argv[])
{
    int *capacity = malloc(sizeof(int)); // creates pointer for integer capacity
    *capacity = 5;                          // assigns capacity to 5
    int *nums = calloc(*capacity, sizeof(int)); // creates array of integers of length capacity
    build_array(nums, argv, argc, capacity); //calls build array function
    sort_array(nums, argc -1);                  // calls sort array function

    int *num_len = malloc(sizeof(int));     // creates pointer to length of number struct array
    *num_len = 1;
    Number *numbers = calloc(1, sizeof(Number));    // creates number struct array

    count_numbers(numbers, nums, argc - 1, num_len); // calls count numbers function

    int *freq_len = malloc(sizeof(int));        // creates pointer to length of frequent numbers array
    *freq_len = 1;
    int *freq = calloc(*freq_len, sizeof(int)); // creates array array for frequent numbers

    find_frequent(freq, freq_len, numbers, num_len);    //calls find frequent

    print_frequents(freq, freq_len, numbers, num_len);  //prints frequent numbers

    return 0;
}

/* full implementations of functions */
// builds array of integers
void build_array(int *n, char* argv[], int len, int *cap)
{
    for (int i = 0; i < len - 1; ++i)   //loops through argv
    {
        if (i == *cap)
        {
            int *tmp = NULL;
            *cap += 1;
            tmp = realloc(n, *cap * sizeof(int)); // reallocates memory
            n = tmp;
        }
        *(n + i) = atoi(*(argv + i + 1)); // assigns values to nums array
    }
}

// sorts array of integers
void sort_array(int *nums, int len) // uses bubble sort
{
    int changes = 0;
    do
    {
        changes = 0;
        for (int i = 0; i < len - 1; ++i)
        {
            if (*(nums + i) > *(nums + i + 1))  // finds number to swap
            {
                swap(nums + i, nums + i + 1);   // calls swap function
                ++changes;
            }
        }
    }
    while (changes != 0);
}

// swaps two integers
void swap(int *a, int *b)
{
    int tmp = *a;                   //assigns temporary variable to address of a
    *a = *b;                        //assigns value at address of a to value at address of b
    *b = tmp;                       //assigns value at address of b to value of twmporary variable
}

// finds current number in list of Numbers and increases by one, otherwise reallocate memory for another Number and add new Number
void count_numbers(Number *numbers, int *nums, int len, int *num_len)
{
    *(numbers) = create_num(*(nums)); // creates first Number struct
    for (int i = 1; i < len; ++i)   // loops through nums array
    {
        int j = 0;
        while (j < *num_len)    //loops through list of Number structs
        {
            if ((numbers + j)->number == *(nums + i)) // check if current number equals current Number struct number value
            {
                (numbers + j)->count += 1;
                break;
            }
            ++j;
        }
        if (j == *num_len)  // if Number struct doesnt exist, adds new struct to list
        {
            ++(*num_len);
            Number *tmp = NULL;
            tmp = realloc(numbers, *num_len * sizeof(Number)); // reallocate memory for new structs
            numbers = tmp;
            *(numbers + j) = create_num(*(nums + i)); // creates new struct
        }
    }
}

// create new Number
Number create_num(int n)
{
    Number num;
    num.number = n;
    num.count = 1;
    return num;
}

// creates new array of frequent numbers
void find_frequent(int *freq, int *freq_len, Number *numbers, int *num_len)
{
    for (int i = 0; i < *num_len; ++i)
    {
        if ((numbers + i)->count > 3) // checks if it occurs more than 3 times
        {
            *(freq + *freq_len - 1) = (numbers + i)->number; // adds frequent number to frequent numbers list
            ++(*freq_len);
        }
        int *tmp = NULL;
        tmp = realloc(freq, *freq_len * sizeof(int)); // reallocates memory
        freq = tmp;
    }
}

// finds the Number struct associated with current frequent number and print that number Number.count times
void print_frequents(int *freq, int *freq_len, Number *numbers, int *num_len)
{
    for (int i = 0; i < *freq_len; ++i) // loops through list of frequents numbers
    {
        int num = 0;
        for (int j = 0; j < *num_len; ++j) // loops through list Number structs
        {
            if ((numbers + j)->number == *(freq + i))
            {
                num = (numbers + j)->count; // assigns struct to current num
                break;
            }
        }
        for (int j = 0; j < num; ++j)
        {
            printf("%d\n", *(freq + i)); // print num current Number.count times
        }
    }
}