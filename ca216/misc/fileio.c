#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* file_input(char *filename) {
    FILE *file = NULL;
    file = fopen(filename, "r");

    char *input = malloc(sizeof(file));

    char *line = malloc(sizeof(char*));
    int i = 0;
    fread(input, sizeof(file), 1, file);
    fclose(file);

    return input;
}

char ** file_output(char *filename) {
    return malloc(sizeof(char**));
}