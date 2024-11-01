/*
Author: Ethan Kavanagh
Date: 03/11/2022
Description: Program creates items to be put into a shopping cart.
    Each item consists of a name, amount, price, and whether it is onsale or not.
    Must determine if an item is onsale or not.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct {
    char *item;
    unsigned int amount;
    float price;
    int promotion;
} Item;                         //declares the Item class and its attributes

/* function prototypes */
void fill_cart(Item *pc, char *argv[], int len, int *pl);
void print_status(Item *pc, int *pl);
char *sale_or_no_sale(int n);

/* main function */
int main(int argc, char* argv[])
{
    Item cart[100];                             //create an array of Items called cart of max len 100
    Item *pcart = &cart[0];                     //creates a pointer pointing to first element of cart

    int length = 0;                             //initializes length of cart array
    int *plength = &length;                     //creates a pointer pointing to address of length

    fill_cart(pcart, argv, argc - 1, plength);  //calls function to create items and fill cart

    print_status(pcart, plength);               //clls function to print the items of the cart and if theyre on sale or not

    return 0;
}

/* full implementations of functions */

// creates the items and adds them to cart
void fill_cart(Item *pc, char *argv[], int len, int *pl)
{
    for (int i = 0; i < len / 4; ++i)                       //loops through the array cart
    {
        (pc + i)->item = *(argv + (i * 4 + 1));             //assigns the item name value to current item
        (pc + i)->amount = atoi(*(argv + (i * 4 + 2)));     //assigns the item amount value to current item
        (pc + i)->price = atof(*(argv + (i * 4 + 3)));      //assigns the item price value to current item
        (pc + i)->promotion = atoi(*(argv + (i * 4 + 4)));  //assigns the promotion value to current item

        ++(*pl);                //increase variable for length of cart array
    }
}

// prints the items from the cart
void print_status(Item *pc, int *pl)
{
    for (int i = 0; i < *pl; ++i)                               //loops through the items in the cart array
    {
        char *status = sale_or_no_sale((pc + i)->promotion);    //calls function to determine if the item is on sale or not
        printf("%s,%d,%.2f,%s\n", (pc + i)->item, (pc + i)->amount, (pc + i)->price, status);   //prints the item details
    }
}

// determines if an item is on sale or not
char *sale_or_no_sale(int n)
{
    if (n == 1)             //checks if items promotion value is 1 for 'On Sale' or other for 'No Sale'
        return "On Sale";
    else
        return "No Sale";
}