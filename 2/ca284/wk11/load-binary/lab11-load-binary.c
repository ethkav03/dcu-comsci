/*
Author: Ethan Kavanagh
Date: 24/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
    char *college;
    int age;
    float grade;
} Student;

/* function prototypes */
void read_student(FILE *file, Student *student);
void print_student(Student *student);

/* main function */
int main(int argc, char* argv[])
{
    FILE *file = NULL;
    Student *student;

    read_student(file, student);

    print_student(student);

    return 0;
}

/* full implementations of functions */
void read_student(FILE *file, Student *student)
{
    char *filename = "studentBinary.bin";
    file = fopen(filename, "rb");
    if(!file)
        printf("Failed to open %s.\n", filename);

    int *name_len = malloc(sizeof(int));
    fread(name_len, sizeof(int), 1, file);

    student->name = calloc(sizeof(char), *name_len);
    fread(student->name, sizeof(char), *name_len, file);

    int *college_len = malloc(sizeof(int));
    fread(college_len, sizeof(int), 1, file);

    student->college = calloc(sizeof(char), *college_len);
    fread(student->college, sizeof(char), *college_len, file);

    int *age = malloc(sizeof(int));
    fread(age, sizeof(int), 1, file);
    student->age = *age;

    float *grade = malloc(sizeof(float));
    fread(grade, sizeof(float), 1, file);
    student->grade = *grade;
}

void print_student(Student *student)
{
    printf("Name: %s\n", student->name);
    printf("College: %s\n", student->college);
    printf("Age: %d\n", student->age);
    printf("Grade: %.2f\n", student->grade);
}