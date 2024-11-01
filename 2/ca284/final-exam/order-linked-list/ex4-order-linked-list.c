/*
Author: Ethan Kavanagh
Date: 13/12/2022
Description: The program checks if the list of number is in sorted (in descending order) or not
Approach: Build a list of numbers from argv. Construct the double linked list to store those numbers. Check to see
    if list is sorted or not, by conducting a single loop of bubble sort inspired algorithm. If no 'swaps' occur,
    then the list is in descending order, otherwise it is not.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct Node Node;

struct Node {       // node struct
    Node *prev;
    int data;
    Node *next;
};

/* function prototypes */
void memory_exit();
void build_array(char *argv[], int len, int *nums);
Node *build_list(int *nums, int n, Node *linked, int i, Node *prev);
int check_order(Node *curr, Node *prev);
void free_memory(Node *list);

/* main function */
int main(int argc, char* argv[])
{
    int *nums = calloc(argc - 1, sizeof(int));  // allocates memory for array of numbers
    if (!nums)          // checks if memory allocation was succesful
        memory_exit();  // calls exit function on  memory allocation failure

    build_array(argv, argc - 1, nums);  // calls build_array function

    Node *head = malloc(sizeof(Node));  // allocates memory for doubly linked list head
    if (!head)          // checks if memory allocation was succesful
        memory_exit();  // calls exit function on  memory allocation failure

    Node *tail = malloc(sizeof(Node));  // allocates memory for doubly linked list tail
    if (!tail)          // checks if memory allocation was succesful
        memory_exit();  // calls exit function on  memory allocation failure

    tail = build_list(nums, argc - 1, head, 0, NULL); // calls function to build doubly linked list and assigns return value to tail
    free(nums); // frees nums

    printf("%d\n", check_order(head, NULL)); //prints result

    free_memory(head);      // frees linked list memory

    return 0;
}

/* full implementations of functions */

// exit due to memory allocation failure
void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// converts command args to array
void build_array(char *argv[], int len, int *nums)
{
    for (int i = 0; i < len; ++i)   // loops through argc
    {
        *(nums + i) = atoi(*(argv + i + 1));    // adds numbers to array from argv
    }
}

// Build Doubly Linked List from array recursively, return tail
Node *build_list(int *nums, int n, Node *linked, int i, Node *prev)
{
    if (i == n)
    {
        linked = NULL;      // base case, sets node to NULL
        return prev;
    }
    linked->prev = prev;                    //  assigns prev to node
    linked->data = *(nums + i);             //  assigns num to data to Node
    linked->next = malloc(sizeof(Node));    //  creates new node for the next
    return build_list(nums, n, linked->next, i + 1, linked);    // recalls function on next node
}

// checks the order of the list
int check_order(Node *curr, Node *prev)
{
    if (curr == NULL)   // base case, checks  for end of list, return 1
        return 1;
    else if (prev != NULL && prev->data < curr->data)   // if a 'swap' occurs return 0
    {
        return 0;
    }
    return check_order(curr->next, curr);  // recalls function on next node
}

// Free memory of doubly linked list
void free_memory(Node *list)
{
    if (list == NULL)
        return free(list);      // base case, end of list
    free_memory(list->next);    // recalls function on next node
    return free(list);          // frees memory of current node
}