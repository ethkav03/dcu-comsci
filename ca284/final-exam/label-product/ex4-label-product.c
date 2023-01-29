/*
Author: Ethan Kavanagh
Date: 13/12/2022
Description: Takes in multiple products. Determines whether their sales are above or below average and what
    what country they cam from/
Approach: Construct an array of products recursively. Calculate average sales of all products recursively. Compare
    the sales of each product to the average. Update the status for each product recursively.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* class definitions */
typedef struct Product Product;

struct Product {        // doubly linked list for Product
    Product *prev;
    char *code;
    float price;
    unsigned int sold;
    int status;
    Product *next;
};

/* function prototypes */
void memory_exit();
Product *get_products(char *args[], int len, Product *linked, int i, Product *prev);
void calc_average(Product *head, float *average, int len);
float count_sales(Product *curr);
float curr_sales(Product *curr);
void update_status(Product *curr, float *average);
void print_list(Product *linked);
char *find_country(char *code);
void free_memory(Product *list);

/* main function */
int main(int argc, char* argv[])
{
    int len = (argc - 1) / 3;       // number of products
    Product *head, *tail;           // initilises had and tail of list
    head = malloc(sizeof(Product)); // allocates memory for had of doubly linked list
    if (!head)              // checks if memory allocation failed
        memory_exit();      // calls memory allocation failure function
    tail = get_products(argv, len, head, 0, NULL);  // calls function to create doubly linked list, returns reference to tal

    float *average = malloc(sizeof(float)); // allocates memory for average sales
    if (!average)       // checks if memory allocation failed
        memory_exit();      // calls memory allocation failure function
    calc_average(head, average, len);   // calls function to calculate average sales recursively

    update_status(head, average);   // calls function to update statuses recursively
    free(average);      // frees memory of average

    print_list(head);   // prints list recursivly

    free_memory(head);     // calls function to free doubly linked list recursively

    return 0;
}

/* full implementations of functions */

// exit due to memory allocation failure
void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// Build Doubly Linked List from array recursively, return tail
Product *get_products(char *args[], int len, Product *linked, int i, Product *prev)
{
    if (i == len)
    {
        linked = NULL;  // base case, end of list of nums
        return prev;
    }
    linked->prev = prev;    // assigns prev to previus product
    linked->code = *(args + (i * 3 + 1));           //
    linked->price = atof(*(args + (i * 3 + 2)));    //  assigns attributes to product
    linked->sold = atoi(*(args + (i * 3 + 3)));     //
    linked->status = 0;                         // defaults status to 0
    linked->next = malloc(sizeof(Product));     // allocates memory for next product
    return get_products(args, len, linked->next, i + 1, linked);    // recalls function on next product
}

// calculates average of all sales
void calc_average(Product *head, float *average, int len)
{
    int total = count_sales(head); // assigns total sales to return value of count_sales function
    *average = total / len;         // sets average to the average sales
}

// counts the total sales recursively
float count_sales(Product *curr)
{
    if (curr->next == NULL)     // base case, end of list
        return curr_sales(curr);
    return curr_sales(curr) + count_sales(curr->next);  // recursively adds sales
}

// return sales of current product
float curr_sales(Product *curr)
{
    return curr->price * curr->sold; // current price multiplied by current units sold
}

// updates the status of each product recursively
void update_status(Product *curr, float *average)
{
    if (curr == NULL)       // base case, end of list
        return;
    else if (curr_sales(curr) >= *average)
        curr->status = 1;           // if sales is above average, set status to 1
    else
        curr->status = 0;           // otherwise, set status to -
    return update_status(curr->next, average);  // recall the function on the next product
}

// Print doubly linked list in reverse
void print_list(Product *linked)
{
    if (linked->next == NULL)
        return;                 // base case, end of list
    printf("%d\n", linked->status);     // prints product status
    printf("%s\n", find_country(linked->code));     // calls function to find the origin country, prints result
    return print_list(linked->next);        // recalls recursive function on next product
}

// finds the origin country
char *find_country(char *code)
{
    switch (*(code) + *(code + 1))  // switch statement, first 2 characters of item code, returns country matching code
    {
        case 'I' + 'E':
            return "Ireland";
        case 'F' + 'R':
            return "France";
        case 'S' + 'P':
            return "Spain";
        case 'U' + 'S':
            return "USA";
        case 'R' + 'U':
            return "Russia";
    }
}

// Free memory of doubly linked list
void free_memory(Product *list)
{
    if (list == NULL)       // base case, end of list
        return free(list);      
    free_memory(list->next);    // recalls recursive fuction
    return free(list);      // frees current
}