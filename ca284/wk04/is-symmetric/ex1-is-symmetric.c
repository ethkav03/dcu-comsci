/*
Author: Ethan Kavanagh
Date: 06/10/2022
Description: Program checks if the string entered is symmetric ie. the same spelt forwards and backwards
*/

/* include libraries */
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/* function prototypes */
bool is_symmetric(char word[]);

/* main function */
int main(int argc, char* argv[])
{
    if (is_symmetric(argv[1]))
        printf("yes\n");
    else
        printf("no\n");

    return 0;
}

/* full implementations of functions */

/* function that determines if string is symmetric or not */
bool is_symmetric(char word[])
{
    char reverse[strlen(word)];
    strcpy(reverse, word); // makes identical copy of word
    for (int i = 0; i < strlen(word); ++i)
    {
        reverse[i] = word[strlen(word) - 1 - i]; // reverses the word
    }

    return strcmp(word, reverse) == 0; // compares word to reverse
}