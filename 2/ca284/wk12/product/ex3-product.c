/*
Author: Ethan Kavanagh
Date: 30/11/2022
Description: Read country information into a structure and a linked list, increase the Ireland price and print.
Approach: Build the Linked List of Product structs.  Increase the price of Ireland product using recursive function. Print country
    information recursively.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* class definitions */
typedef struct Product Product;

struct Product {
    char *code;
    char *country;
    int price;
    Product *next;
};

/* function prototypes */
void build_array(char *argv[], int argc, Product *product);
void increase(Product *product);
void print_array(Product *product);

/* main function */
int main(int argc, char* argv[])
{
    Product *product = calloc(1, sizeof(product)); // creates head of the linked list

    build_array(argv, argc, product); // calls build array function

    increase(product); // calls increase function

    print_array(product); // calls print function

    return 0;
}

/* full implementations of functions */
// function to build linked list
void build_array(char *argv[], int argc, Product *product)
{
    Product *curr = product;
    Product *next;
    for (int i = 0; i < (argc - 1) / 3; ++i) // loops through argv countries informations
    {
        curr->code = *(argv + (i * 3) + 1); // assigns product code
        curr->country = *(argv + (i * 3) + 2); // assigns country
        curr->price = atoi(*(argv + (i * 3) + 3)); // assigns product price

        if (i == (argc - 1) / 3 - 1)
            curr->next = NULL; // sets NULL to end of linked list
        else
            curr->next = calloc(1, sizeof(Product)); // assigns new Product to current next
        curr = curr->next;
    }
}

// function to calculate and add increase to irish products recursively
void increase(Product *product)
{
    if (product == NULL)
        return;
    if (strcmp(product->country, "Ireland") == 0) // irish countries
    {
        int increase = product->price * .2; // calculates increas
        product->price = product->price + increase; // increases price
    }
    return increase(product->next);
}

// function to print country information recursively
void print_array(Product *product)
{
    if (product == NULL)
        return;
    printf("%s\n", product->code);
    printf("%s\n", product->country);
    printf("%d\n", product->price);
    return print_array(product->next);
}