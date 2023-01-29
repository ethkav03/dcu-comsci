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
Node *get_node(int *arr, int n);
void insert(Node *list, int pos, int num);
void print_list(Node *list);

/* main function */
int main(int argc, char* argv[])
{
    int parr[] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};
    int *arr = &parr[0];
    int len = 10;

    Node *start = NULL;

    start = get_node(arr, len);

    int pos = atoi(argv[1]);
    int num = atoi(argv[2]);

    insert(start, pos, num);

    print_list(start);

    return 0;
}

/* full implementations of functions */
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

void insert(Node *list, int pos, int num)
{
    Node *curr, *next;
    curr = list;
    while (curr->next != NULL && curr->value != pos)
    {
        
        curr = curr->next;
        next = curr->next;
    }
    if (curr->next = NULL)
        return;

    curr->next = calloc(1, sizeof(Node));
    curr->next->value = num;
    curr->next->next = next;
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