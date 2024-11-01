/*
    Author: Ethan Kavanagh
    Date: 29/09/2022
    Description: Program that reveres the order of a string
*/
/* include relevant libraries */
#include <stdio.h>
#include <string.h>

/* function prototypes */
void reverse(char s[50]);

/* main function */
int main(int argc, char * argv[])
{
	if (argc > 2)
    {
        printf("Too many arguments.\n");
        return 1;
    }
    if (argc < 2)
    {
        printf("Too few arguments.\n");
        return 1;
    }

    reverse(argv[1]);
	return 0;
}

/* actual implementation of the functions */
void reverse(char s[50])
{
    char t[50];
    strcpy(t, s);
    for (int i = 0; i < strlen(s); ++i)
    {
        t[i] = s[strlen(s) - 1 - i];
    }
    
    printf("%s\n", t);
}