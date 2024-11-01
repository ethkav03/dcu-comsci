/*
Author: Ethan Kavanagh
Date: 30/11/2022
Description: Read in a number of integers and determine how many times the most commonly occuring number occurs.
Approach: Read all integers into an array. Sort the array in ascending order. Build the linked list of numbers. Find how many times the
    most commonly occuring number occurs. Print the result.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct Number Number;

struct Number{
    int number;
    int count;
    Number *next;
};

/* function prototypes */
void build_array(int *nums, int len, char *args[]);
void sort_array(int *nums, int len);
void swap(int *a, int *b);
void create_list(int *nums, int len, Number *number);
void find_highest(Number *number, int *high);

/* main function */
int main(int argc, char* argv[])
{
    int *nums = calloc(argc - 1, sizeof(int)); // creates array for the integers
    build_array(nums, argc, argv);  // calls the function to build the array

    sort_array(nums, argc - 1); // calls the function to sort that array

    Number *number = malloc(sizeof(Number));    // initializes the head of the linked list

    create_list(nums, argc, number);    // calls function to create linked list

    int *highest = malloc(sizeof(int)); // initializes integer to store highest occurences
    *highest = 0;
    find_highest(number, highest);  //calls function to find the highest occuring number

    printf("%d\n", *highest);   // prints result

    return 0;
}

/* full implementations of functions */
// builds array of integers
void build_array(int *nums, int len, char *args[])
{
    for (int i = 0; i < len - 1; ++i) // loops through command line arguments
    {
        *(nums + i) = atoi(*(args + i + 1)); // assigns values from argv to nums
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

// builds the linked list
void create_list(int *nums, int len, Number *number)
{
    Number *curr = number;  // stores reference to head of list
    Number *check = number;
    curr->number = *(nums);
    curr->count = 1;       //         initialises head of linked list
    curr->next = NULL;
    for (int i = 1; i < len - 1; ++i)   // loops through array of integers
    {
        while (check != NULL)   // traverses through linked list
        {
            if (*(nums + i) == check->number)   // checks if current number in array is equal to a number in linked list
            {
                check->count += 1;  // if yes increase that numbers number of occurences
                break;
            }
            check = check->next;    // pther wise continue
        }
        if (check == NULL)  // if no matching node is found, create new node
        {
            curr->next = malloc(sizeof(Number));    // assign memory for new node
            curr = curr->next;
            curr->number = *(nums + i);         // assign attribute of new node
            curr->count = 1;
            curr->next = NULL;
            check = curr;
        }
    }
}

// finds occurences of most commonly occuring number recursively
void find_highest(Number *number, int *high)
{
    if (number->next == NULL)   // checks for tail of list
        return;
    if (number->count > *high)  // checks if occurences are higher
    {
        *high = number->count;      // overwrites highest occurences
    }
    return find_highest(number->next, high);    // calls recursive function
}