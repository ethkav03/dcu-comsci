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
    int value;
    Node *next;
};

/* function prototypes */
void build_array(int *arr, int len, char * argv[]);
Node *get_node(int *arr, int n);
void pop(Node *list);
void push(Node *list, int n);
void print_list(Node *list);

/* main function */
int main(int argc, char* argv[])
{
    //printf("%ld\n", sizeof(Node));

    int count = atoi(argv[1]);
    int *arr = calloc(count, sizeof(int));

    build_array(arr, count, argv);

    Node *start = NULL;

    start = get_node(arr, count);

    pop(start);
    pop(start);

    push(start, atoi(argv[argc - 2]));
    push(start, atoi(argv[argc - 1]));

    print_list(start);
    //printf("\n");

    return 0;
}

/* full implementations of functions */
void build_array(int *arr, int len, char * argv[])
{
    for (int i = 0; i < len; ++i)
    {
        *(arr + i) = atoi(*(argv + i + 2));
    }
}

Node *get_node(int *arr, int count)
{
    Node *current, *first; /*declare two pointers */
	int selection; /* to ask if the user keep entering new student data or stop */


	first = (Node*)calloc(1,sizeof(Node)); /*create the first node */
	current = first; /*Now the current node is also the first node */
    int i = 0;
	while(i < count)
	{
		/* allocate node and change the current point */
		current->value = *(arr + i);
		i += 1;
		if (i < count)
			current->next = (Node*)calloc(1, sizeof(Node));
		else
			current->next = NULL;
		//printf("Arr[i]: %d, Value: %d, Next: %p\n", *(arr + i), current->value, current->next);
		//printf("Value: %d, Next: %p\n", current->value, current->next);
		current = current->next;
	}
	return first; /* return the address of the first node */
}

void pop(Node *list)
{
    Node *curr = list;
    while (curr->next->next != NULL)
    {
        //printf("Value: %d, Next: %p\n", curr->value, curr->next);
        curr = curr->next;
    }
	//printf("Value: %d, Next: %p\n", curr->value, curr->next);
    curr->next = NULL;
	//printf("Value: %d, Next: %p\n", curr->value, curr->next);
}

void push(Node *list, int n)
{
    Node *curr = list;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }

    Node *node = calloc(1, sizeof(Node));
    node->value = n;
    node->next = NULL;
    curr->next = node;
    return;
}

void print_list(Node *list)
{
    if (list == NULL)
    {
        return;
    }
    printf("%d\n", list->value);
    return print_list(list->next);
}