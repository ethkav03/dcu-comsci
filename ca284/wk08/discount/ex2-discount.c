/*
Author: Ethan Kavanagh
Date: 03/11/2022
Description: Program creates items to be put into a shopping cart.
    Each item consists of a name, amount, price, and whether it is onsale or not.
    Calculates the total amount to be paid for all items.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* class definitions */
typedef struct {
    char *item;
    unsigned int amount;
    float price;
    int promotion;
} Item;                         //declares the Item class and its attributes

/* function prototypes */
void fill_cart(Item *pc, char *argv[], int len, int *pl);
void calculate_total(Item *pc, float *tot, int *len);
float calc_discount(Item c);

/* main function */
int main(int argc, char* argv[])
{
    Item cart[100];                             //create an array of Items called cart of max len 100
    Item *pcart = &cart[0];                     //creates a pointer pointing to first element of cart

    int length = 0;                             //initializes length of cart array
    int *plength = &length;                     //creates a pointer pointing to address of length

    fill_cart(pcart, argv, argc - 1, plength);  //calls function to create items and fill cart

    float total = 0;                            //initializes variable for total cost
    float *ptotal = &total;                     //creates a pointer pointing to total

    calculate_total(pcart, ptotal, plength);    //calls function to calculate total cost

    printf("%.2f\n", *ptotal);              //prints the total cost

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

// calculates the total price to be paid
void calculate_total(Item *pc, float *tot, int *len)
{
    for (int i = 0; i < *len; ++i)                              //loops through items in cart
    {
        if ((pc + i)->promotion == 1)                           //checks if item is on sale or not
            *tot += calc_discount(*(pc + i));                   //adds cost of discounted items to total cost
        else
            *tot += (float)(pc + i)->amount * (pc + i)->price;  //adds cost of items to total cost
    }
}

// calculates the price to be paid for the discounted item
float calc_discount(Item c)
{
    int free_items = abs(c.amount / 3);         //calculates how many items are free
    return (c.amount - free_items) * c.price;   //takes away free items from total items, then multiplies by item price,
}                                               //to get cost of discounted items