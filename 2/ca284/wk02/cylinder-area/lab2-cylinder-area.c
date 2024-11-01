#include <stdio.h>
#include <stdlib.h>

#define PI 3.1415 // Defines a constant PI

int main(int argc, char* argv[])
{
    if (argc == 1)                  //
    {                               // Checks for no
        printf("No input given!");  // arguments
        return 1;                   //
    }
    if (argc == 2)                          //
    {                                       // Checks for more
        printf("Two arguments needed!");    // than 1 argument
        return 1;                           //
    }

    int r = atoi(argv[1]); // Initializes height
    int h = atoi(argv[2]); // Initializes radius

    if (h < 0 || r < 0)                                         //
    {                                                           // Checks for
        printf("The radious or height cannot be negative!");    // negative number
        return 1;                                               //
    }

    float area = 2*PI*r*h + 2*PI*r*r; // Calculates area

    printf("%.2f\n", area); // Prints area

    return 0;
}