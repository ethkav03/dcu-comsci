/*
Author: Ethan Kavanagh
Date: 10/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* class declarations */
typedef struct {
    char * name[20];
    char * programme[20];
    float grade;
} Student;

/* function prototypes */
void exit_program();
void build_array(Student *students, int *len, char *argv[]);
void calc_average(int *len, Student *students, float *average);
void print_array(Student *students, int *len, float *average);

/* main function */
int main(int argc, char* argv[])
{
    int *len = calloc(1, sizeof(int));
    if (!len)
    {
        exit_program();
    }
    *len = (argc - 1) / 3;
    //printf("%d\n", *len);

    Student *students = calloc(*len, sizeof(Student));
    if (!students)
    {
        exit_program();
    }

    build_array(students, len, argv);

    float *average = calloc(1, sizeof(float));
    if (!average)
    {
        exit_program();
    }
    *average = 0;
    calc_average(len, students, average);

    print_array(students, len, average);

    free(students);
    free(len);

    printf("Average grade: %.2f\n", *average);
    free(average);

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
        *(students + i - 1)->name = *(argv + ((i - 1) * 3 + 1));
        *(students + i - 1)->programme = *(argv + ((i - 1) * 3) + 2);
        (students + i - 1)->grade = atof(*(argv + ((i - 1) * 3) + 3));
    }
}

void calc_average(int *len, Student *students, float *average)
{
    for (int i = 0; i < *len; ++i)
    {
        *average += (students + i)->grade;
        //printf("%.2f\n", (students + i)->grade);
    }
    *average = *average / *len;
}

void print_array(Student *students, int *len, float *average)
{
    for (int i = 0; i < *len; ++i)
    {
        if ((students + i)->grade > *average && strcmp(*(students + i)->programme, "CSCE") == 0)
        {
            printf("%s, %.2f\n", *(students + i)->name, (students + i)->grade);
        }
        //printf("%s, %.2f\n", *(students + i)->name, (students + i)->grade);
    }
}