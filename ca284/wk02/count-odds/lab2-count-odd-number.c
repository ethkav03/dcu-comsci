#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int values[10]; //Initializes array of max length 10
    int count = 0;

    for (int i = 1; i < argc; ++i)
    {
        values[i - 1] = atoi(argv[i]); //Converts char to int and store in values array
        if (values[i - 1] % 2 == 1)    //
        {                              // Increases count variable
            ++count;                   // if odd number found
        }                              //
    }
    printf("%d\n", count);

    return 0;
}
