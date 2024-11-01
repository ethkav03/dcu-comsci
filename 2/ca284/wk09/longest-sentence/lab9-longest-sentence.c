/*
Author: Ethan Kavanagh
Date: 10/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* function prototypes */
void exit_program();
int find_longest(int len, char *args[]);
void build_array(char **words, int len, char *argv[]);
void find_highest(char **words, int len, int *highest);
void print_array(char **words, int len, int *highest);

/* main function */
int main(int argc, char* argv[])
{
    char **words = calloc(argc - 1, sizeof(char*));
    if (!words)
        exit_program();

    build_array(words, argc - 1, argv);

    int *highest = calloc(1, sizeof(int));
    if (!highest)
        exit_program();
    *highest = 0;

    find_highest(words, argc - 1, highest);


    print_array(words, argc - 1, highest);

    free(words);
    free(highest);

    return 0;
}

/* full implementations of functions */
void exit_program()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

void build_array(char **words, int len, char *argv[])
{
    for (int i = 0; i < len; ++i)
    {
        *(words + i) = *(argv + i + 1);
    }
}

void find_highest(char **words, int len, int *highest)
{
    for (int i = 0; i < len; ++i)
    {
        if (strlen(*(words + i)) > *highest)
        {
            *highest = strlen(*(words + i));
        }
    }
}

void print_array(char **words, int len, int *highest)
{
    for (int i = 0; i < len; ++i)
    {
        if (strlen(*(words + i)) == *highest)
        {
            printf("%s\n", *(words + i));
        }
    }
}