#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ARGS 16
#define SEPARATORS " \t\n"

char* read_input() {
    char *input = NULL;
    size_t buflen = 0;
    getline(&input, &buflen, stdin); // takes line input
    return input;
}
/*
    Tutorial - Write a Shell in C
    https://brennan.io/2015/01/16/write-a-shell-in-c/
*/

char** split_input(char *input) {
    int length = 0;
    int capacity = MAX_ARGS;
    char **args = malloc(capacity * sizeof(char*)); // array of arguments

    char *arg = strtok(input, SEPARATORS); // splits input into arguments

    while (arg != NULL) {
        args[length] = arg; // adds argument to array
        length++;   // increases size of arguments array to accomodate more arguments

        if (length >= capacity) {   // checks if number of arguments is less than max arguments and reallocates memory accordingly
            capacity = (int) (capacity * 1.5);
            args = realloc(args, capacity * sizeof(char*));
        }

        arg = strtok(NULL, SEPARATORS);
    }

    args[length] = NULL;
    return args;
}
/*
    Tutorial - Write a Shell in C
    https://brennan.io/2015/01/16/write-a-shell-in-c/
*/