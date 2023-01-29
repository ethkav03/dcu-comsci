/*
Author: Ethan Kavanagh
Date: 10/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class declarations */
typedef struct {
    char * name[20];
    char * programme[20];
    float grade;
} Student;

/* function prototypes */
void exit_program();
void build_array(Student *students, int *len, char *argv[]);
void print_array(Student *students, int *len);

/* main function */
int main(int argc, char* argv[])
{
    int *len = calloc(1, sizeof(int));
    if (!len)
    {
        exit_program();
    }
    *len = (argc - 1) / 3;

    Student *students = calloc(*len, sizeof(Student));
    if (!students)
    {
        exit_program();
    }

    build_array(students, len, argv);

    print_array(students, len);

    free(students);
    free(len);

    return 0;
}

/* full implementations of functions */
void exit_program()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

void build_array(Student *students, int *len, char *argv[])
{
    for (int i = 1; i < *len + 1; ++i)
    {
        *(students + i)->name = *(argv + ((i - 1) * 3 + 1));
        *(students + i)->programme = *(argv + ((i - 1) * 3) + 2);
        (students + i)->grade = atof(*(argv + ((i - 1) * 3) + 3));
    }
}

void print_array(Student *students, int *len)
{
    for (int i = 1; i < *len + 1; ++i)
    {
        printf("%s, %s, %.2f\n", *(students + i)->name, *(students + i)->programme, (students + i)->grade);
    }
}