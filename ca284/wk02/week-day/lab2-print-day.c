#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int day, index;
    char* weekdays[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}; //Array of weekday

    day = atoi(argv[1]); //User inputted day of week
    index = day - 1; //Minus one because array starts at 0, prevent segmentation fault

    printf("%s\n", weekdays[index]); //Prints day at index 'index' of 'weekdays'

    return 0;
}
