#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *infile = NULL;
    char *inname = "bin.txt";

    infile = fopen(inname, "r");
    if(!infile)
        printf("Failed to open %s.\n", inname);

    FILE *outfile = NULL;
    char *outname = "bin.bin";

    outfile = fopen(outname, "w");
    if(!outfile)
        printf("Failed to open %s.\n", outname);

    char *name = calloc(4, sizeof(char));
    fread(name, 4, sizeof(char), infile);
    fwrite(name, sizeof(char), 4, outfile);

    char *college = calloc(3, sizeof(char));
    fread(college, 3, sizeof(char), infile);
    fwrite(college, sizeof(char), 3, outfile);

    int *age = malloc(sizeof(int));
    fread(age, 1, sizeof(int), infile);
    fwrite(age, sizeof(int), 1, outfile);

    float *grade = malloc(sizeof(float));
    fread(grade, 1, sizeof(float), infile);
    fwrite(grade, sizeof(float), 1, outfile);
}