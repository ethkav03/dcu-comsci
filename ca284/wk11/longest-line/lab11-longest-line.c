/*
Author: Ethan Kavanagh
Date: 25/11/2022
Description: 
*/

/* include libraries */
//#include <stdio.h>
//#include <stdlib.h>

/* function prototypes */
//void find_len(int *len, FILE *file, char *filename);
//void find_longest(int *start, int *longest, int *len, char *data);
//void print_longest(char *data, int *start, int *longest);

/* main function */
//int main(int argc, char* argv[])
//{
//    FILE *file = NULL;
//    char *filename = "paragraph.txt";

//    int  *len = malloc(sizeof(int));
//    find_len(len, file, filename);
    
//    file = fopen(filename, "r");
//    if(!file)
//        printf("Failed to open %s.\n", filename);

//    char *data = calloc(*len, sizeof(char));
//    fread(data, *len, sizeof(char), file);
    
//    int s = 0;
//    int *start = &s;
//    int *longest = malloc(sizeof(int));

//    find_longest(start, longest, len, data);

//    printf("%d\n", *longest);
//    print_longest(data, start, longest);

//    return 0;
//}

/* full implementations of functions */
//void find_len(int *len, FILE *file, char *filename)
//{
//    file = fopen(filename, "r");
//    if(!file)
//        printf("Failed to open %s.\n", filename);

//    int mchar = fgetc(file);
//    while (mchar != EOF)
//    {
//        ++(*len);
//        mchar = fgetc(file);
//    }
//    fclose(file);
//}

//void find_longest(int *start, int *longest, int *len, char *data)
//{
//    int marker = 0;
//    for (int i = 0; i < *len; ++i)
//    {
//        if (*(data + i) == '.' || *(data + i) == '!' || *(data + i) == '?')
//        {
//            if (i - marker > *longest)
//            {
//                *longest = i - marker + 1;
//                *start = marker + 1;
//            }
//            marker = i + 1;
//        }
//    }
//}

//void print_longest(char *data, int *start, int *longest)
//{
//    for (int i = *start; i < *start + *longest; ++i)
//    {
//        printf("%c", *(data + i));
//    }
//    printf("\n");
//}

#include<stdio.h>
#include<stdlib.h>
#include <string.h>

int main(int argc, char*argv[])
{
    char line[200];
    char max[200]=" ";
 
    FILE *pfile = NULL;
    char *filename = "paragraph.txt";
    pfile = fopen(filename, "r");
    if(!pfile)  // Open myfile.txt to write it
        printf("Failed to open %s.\n", filename);
 
    if(pfile!=NULL)
    {
   	    while(fgets(line,sizeof(line),pfile)!=NULL) // read whole line
        {
            if(strlen(max)<strlen(line))
 	        strcpy(max,line);
 	    }
 	    printf("%d\n", (strlen(max)));
	    printf("%s\n",max);
 	    fclose(pfile);
    }
    return 0;
}