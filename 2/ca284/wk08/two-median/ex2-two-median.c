/*
Author: Ethan Kavanagh
Date: 03/11/2022
Description: Outputs the middle 2 numbers from command line.
    Build array, then sort array (using bubble sort), then print elements at length / 2 and length / 2 + 1.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* function prototypes */
void build_array(int n, char * a[], int *p, int *l);
void sort_array(int *p, int *l);
void swap(int *a, int *b);
void find_middle(int *p, int *l, int *mid);

/* main function */
int main(int argc, char* argv[])
{
    int nums[100];                  //initializes array of length 100
    int *pnums = &nums[0];          //creates a pointer for address of nums

    int len = 0;
    int *plen = &len;

    build_array(argc, argv, pnums, plen);       //calls build function

    sort_array(pnums, plen);                    //calls sort function

    int middle[2];                              //initializes array to store middles numbers
    int *pmiddle = &middle[0];                  //creates a pointer for address of middle

    find_middle(pnums, plen, pmiddle);          //calls function to find the middle numbers

    printf("%d\n", middle[0]);              //prints first middle number
    printf("%d\n", middle[1]);              //prints second middle number

    return 0;
}

/* full implementations of functions */

// builds the array of numbers
void build_array(int n, char * a[], int *p, int *l)
{
    for (int i = 1; i < n; ++i)             //loops through command-line arguments
    {
        *(p + i - 1) = atoi(*(a + i));      //assembles array of numbers
        ++(*l);                             //increases variable tracking length of array by 1
    }
}

// sorts the array of numbers from smallest to largest using bubble sort
void sort_array(int *p, int *l)
{
    int changes;                            //initializes variable to store amount of changes
    do                                      //loop runs minimum once to check if array is sorted or not
    {
        changes = 0;
        for (int i = 0; i < *l - 1; ++i)    //loops through the array of numbers
        {
            if (*(p + i) > *(p + i + 1))    //compares adjacent numbers
            {
                swap(p + i, p + i + 1);     //calls swap function to swap adjacent numbers

                ++changes;                  //increments changes variable
            }
        }
    }
    while (changes > 0);                //checks if changes is greater than 0, if greater loops again
}

// swaps the 2 values by passing by reference
void swap(int *a, int *b)
{
    int tmp = *a;                   //assigns temporary variable to address of a
    *a = *b;                        //assigns value at address of a to value at address of b
    *b = tmp;                       //assigns value at address of b to value of twmporary variable
}

// finds the middle 2 values of the numbers
void find_middle(int *p, int *l, int *mid)
{
    int half = *l / 2;              //finds the midpoint of numbers
    *(mid) = *(p + half - 1);       //finds first middle number
    *(mid + 1) = *(p + half);       //finds second middle number
}