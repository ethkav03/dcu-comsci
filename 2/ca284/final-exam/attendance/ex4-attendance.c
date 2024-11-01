/*
Author: Ethan Kavanagh
Date: 13/12/2022
Description: A program to track a students attendance and determine if they've been absent too often or not. If
    student is absent 3 or more times the get a status of 1. Also if a student is late 3 times in a row, they
    are marked with an additional absence.
Approach: Builds the array from argv. Creates a list of Student structs. Counts how many times a student has been 
    absent or late. Prints the statuses.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* class definitions */
typedef struct {
    int attendance_status;
} Student; // Student struct to track attendence status

/* function prototypes */
void memory_exit();
void build_array(char *argv[], int len, char **atts);
void get_students(int len, char **atts, Student *students);
int count_abs(char *atten);
void print_atten_statuses(int len, Student *students);

/* main function */
int main(int argc, char* argv[])
{
    char **atts = calloc(argc - 1, sizeof(char*)); // allocates memory for attendances
    if (!atts)
        memory_exit();
    build_array(argv, argc - 1, atts);          //calls build array function

    Student *students = calloc(argc - 1, sizeof(Student));  // allocates memory for array of students
    if (!students)
        memory_exit();
    get_students(argc - 1, atts, students); // calls get_students function
    free(atts);     // frees memory in atts

    print_atten_statuses(argc - 1, students); // calls print function
    free(students);         // frees memory in students

    return 0;
}

/* full implementations of functions */

// exit if failled to assign memory
void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// converts command args to array
void build_array(char *argv[], int len, char **atts)
{
    for (int i = 0; i < len; ++i)   // loops through argv
    {
        *(atts + i) = *(argv + i + 1);  // assigns value from argv to new array
    }
}

// populates the status for each student
void get_students(int len, char **atts, Student *students)
{
    int abs;
    for (int i = 0; i < len; ++i)   // loops through student
    {
        abs = count_abs(*(atts + i));   // calls count_abs function and assigns value to abs
        if (abs >= 3)                                   //
            (students + i)->attendance_status = 1;      // if abs is greater than or equal to 3 it assigns status
        else                                            // to 1, otherwise assigns to 0
            (students + i)->attendance_status = 0;      //
    }
}

// counts the number of absences
// loops through all letter in string. If it finds an A it increases abscount by 1. If it finds an L it
//  increases latecount by 1. For each consecutive L it increases count by 1. If it encounters an A or P before
//  another L it resets count to 0. If it finds 3 in a row it increases absence count.
int count_abs(char *atten)
{
    int abscount = 0;   // count of absences
    int latecount = 0;  // count of lates
    for (int j = 0; j < strlen(atten); ++j) // loops through attendances
    {
        if (*(atten + j) == 'A')    // if A
        {
            abscount += 1;          // increase absences by 1
            latecount = 0;          // set latecount back to 0
        }
        else if (*(atten + j) == 'L')   // if L
        {
            latecount += 1;             // increase latecount by 1
        }
        else                    // if P
            latecount = 0;      // set latecount back to 0

        if (latecount == 3)     // if there are 3 consecutive Ls
        {
            abscount += 1;      // increase absences by 1
            latecount = 0;      // set latecount back to 0
        }
    }
    return abscount;
}

//prints the statuses
void print_atten_statuses(int len, Student *students)
{
    for (int i = 0; i < len; ++i)
    {
        printf("%d\n", (students + i)->attendance_status);
    }
}