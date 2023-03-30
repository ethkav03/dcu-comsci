#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "commands.h"
#include "fileio.h"
#include "input.h"

int main(int argc, char *argv[]) {
    bool input = false;
    char *infile = malloc(sizeof(char*));
    bool output = false;
    char *outfile = malloc(sizeof(char*));
    char *symbol = malloc(sizeof(char*));
    int x = 0;

    if (argc > 1) {
        return 0;
    } else {
        while(1) {
            char* pwd = getenv("PWD");
            fprintf(stdout, "~%s$ ", pwd);  // display current directory

            char *readinput = read_input();     // take input from command line
            if (*readinput == '\n') { continue; }

            char **args = split_input(readinput);   //split input into arguments

            char **cmdargs = malloc(sizeof(args));

            int len = 0;
            while (*(args + len)) {
                len++;
            }

            for (int i = 0; i < len; ++i) {
                printf("%s ", *(args + i));
            }
            printf("\n"); 

            if (!strcmp(*(args + (len - 2)), "<")) {
                infile = *(args + (len - 1));
                input = true;
                x = len - 2;
            } else if (!strcmp(*(args + (len - 4)), "<")) {
                infile = *(args + (len - 3));
                input = true;
                x = len - 4;
            }
            if (!strcmp(*(args + (len - 2)), ">") || !strcmp(*(args + (len - 2)), ">>")) {
                outfile = *(args + (len - 1));
                output = true;
                symbol = *(args + (len - 2));
                if (len - 2 < x) {x = len - 2;}
            }

            for (int i = 0; i < x; ++i) {
                *(cmdargs + i) = *(args + i);
            }

            for (int i = 0; i < x; ++i) {
                printf("%s ", *(cmdargs + i));
            }
            printf("\n");

            char * fileinput = malloc(sizeof(char**));

            if (input) {
                fileinput = file_input(infile);
                printf("%s\n", fileinput);
            }
            char ** fileoutput = malloc(sizeof(char**));
            fileoutput = environment();
            int i = 0;
            while(fileoutput + i) {
                printf("%s", *(fileoutput + i));
                i++;
            }
            if (output) {
                file_output(outfile);
            }
        }
    }
    return 0;
}