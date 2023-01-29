#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int values[10]; //Initializes array of max length 10
    int count = 0; //Counts evens

    for (int i = 1; i < argc; ++i)
    {
        values[i - 1] = atoi(argv[i]); //Converts from char to int and stores in values array
        if (values[i - 1] % 2 == 0)
        {
            printf("%i - %i\n", i - 1, values[i - 1]); //Prints index and value
            ++count; //Increments 'count' variable
        }
    }

    if (count == 0)                 //
    {                               // If there is no
        printf("Not found!\n");     // even numbers found 
    }                               //

    return 0;
}