/*
 *  circle-area.c
 *   author <your name>
 *    */

/* includes*/
#include <stdio.h>
#include <stdlib.h> /* contains functions we may need*/

#define PI 3.14 /*Defining PI as a constant*/

/* Function: Main
 *  parameters: int argc (argument count)
 *   char *argv[] an array of command-line arguments
 *   description:  Takes a single argument and computes area of circle
 *    */

int main()
{
  /* variable initialisation */
  int radius = 0;
  int *pradius = &radius;
  float area = 0.0;
  float *parea = &area;
  /* all command-line arguments come in as character strings, so atoi turns them into ints*/
  scanf("%d", pradius);
  if (pradius < 0)
  {
    printf("Enter integer greater than or equal to 0\n");
    return 1;
  }

  pradius = pradius * pradius; /* radius squared */

  parea  = pradius * PI; /* calculate area of circle */

  /* print to two decimal places*/
  printf("%.2f\n", parea); /* We only want to show only two values to the right of the decimal point*/

  return 0; /* exit correctly*/
} /* end program*/
