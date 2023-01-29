/*
Author: Ethan Kavanagh
Date: 17/11/2022
Description: 
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct Node Node;

struct Node {
    float value;
    Node *prev;
    Node *next;
};

/* function prototypes */
void build_array(float *arr, int len, char * argv[]);
Node *get_node(float *arr, int n);
void print_list(Node *start);

/* main function */
int main(int argc, char* argv[])
{
    int count = atoi(argv[1]);
    float *arr = calloc(count, sizeof(float));

    build_array(arr, argc, argv);

    Node *start = NULL;

    start = get_node(arr, count);

    print_list(start);

    return 0;
}

/* full implementations of functions */
void build_array(float *arr, int len, char * argv[])
{
    for (int i = 0; i < len - 2; ++i)
    {
        *(arr + i) = atoi(*(argv + i + 2));
    }
}

Node *get_node(float *arr, int count)
{
    Node *current, *first, *prev;

    first = calloc(1, sizeof(Node));
    current = first;

    int i = 0;
    while (i < count)
    {
        
        current->value = *(arr + i);
        current->next = calloc(1, sizeof(Node));

        prev = current;
        current = current->next;

        i += 1;
    }
    current->next = NULL;
    return first;
}

void print_list(Node *start)
{
    if (start->next == NULL)
        return;
    print_list(start->next);

    printf("%.2f\n", start->value);
}