/*
Author: Ethan Kavanagh
Date: 20/10/2022
Description: 
*/

/* include libraries */
#include <stdio.h>

/* function prototypes */
void print_info(int n, char * info[]);

/* main function */
int main(int argc, char* argv[])
{
    print_info(argc, argv);

    return 0;
}

/* full implementations of functions */
void print_info(int n, char * info[])
{
    printf("%s\n", info[1]);
    printf("%s\n", info[2]);
    printf("%s million people\n", info[3]);
    printf("%s km2\n", info[4]);
}