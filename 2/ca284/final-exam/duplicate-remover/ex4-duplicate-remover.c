/*
Author: Ethan Kavanagh
Date: 13/12/2022
Description: Revome all duplicate numbers from a linked list
Approach: Build array of numbers. Store those numbers in a doubly linked list. Initilize array counts of length largest number of 0s.
    Increment each index of counts by current number in linked list. Remove all duplicate numbers (that occur more than once). Print
    remaining numbers.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>

/* class definitions */
typedef struct Node Node;

struct Node {       // struct to store information of a node
    Node *prev;
    int data;
    int frequency;
    Node *next;
};

/* function prototypes */
void memory_exit();
void build_array(char *argv[], int len, int *nums);
Node *build_list(int *nums, int n, Node *linked, int i, Node *prev);
void reset_counts(int *counts, int *len);
void find_counts(Node *head, int *counts);
void remove_dups(Node *start, int *counts);
void print_list(Node *linked);
void free_memory(Node *list);

/* main function */
int main(int argc, char* argv[])
{
    int *nums = calloc(argc - 1, sizeof(int));  // allocates memory for nums array of ints
    if (!nums)                      // checks for memory allocations failure
        memory_exit();  	        // calls memory failure exit function
    build_array(argv, argc - 1, nums);  // calls function to build array

    Node *head = malloc(sizeof(Node));  // allocates memory for head of linked list
    if (!head)                      // checks for memory allocations failure
        memory_exit();  	        // calls memory failure exit function

    Node *tail = malloc(sizeof(Node));  // allocates memory for tail of linked list
    if (!tail)                      // checks for memory allocations failure
        memory_exit();  	        // calls memory failure exit function

    tail = build_list(nums, argc - 1, head, 0, NULL); // calls function to build doubly linked list, store refernce in tail

    int *counts = calloc(*(nums + argc - 2), sizeof(int));  // allocate memory for counts
    if (!counts)                      // checks for memory allocations failure
        memory_exit();  	        // calls memory failure exit function
    reset_counts(counts, nums + argc - 2);  // calls function to fill counts array with 0s

    find_counts(head, counts);  // updates the count of each number

    remove_dups(head, counts);  // removes all duplicates from doubly linked list

    print_list(head);   // prints doubly linked list

    free_memory(head);  // frees memory of doubly linked list

    return 0;
}

/* full implementations of functions */

// failed memory allocation
void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// converts command args to array
void build_array(char *argv[], int len, int *nums)
{
    for (int i = 0; i < len; ++i)   // loops through argv
    {
        *(nums + i) = atoi(*(argv + i + 1));    // assigns values of argv to nums
    }
}

// Build Doubly Linked List from array, return tail
Node *build_list(int *nums, int n, Node *linked, int i, Node *prev)
{
    if (i == n) // if current num equal to len n
    {
        linked = NULL;  // set end to NULL
        return prev;    // return previous node for tail
    }
    linked->prev = prev;        // set current prev to prev
    linked->data = *(nums + i); // set current data to current num
    linked->next = malloc(sizeof(Node));    // allocate memory for new node
    return build_list(nums, n, linked->next, i + 1, linked);    // recalls function on next node
}

// resets all numbers in counts to 0
void reset_counts(int *counts, int *len)
{
    for (int i = 0; i < *len; ++i)  // loops through all numbers in counts
    {
        *(counts + i) = 0;  // sets each one to 0
    }
}

// updates the count of each number in counts
void find_counts(Node *head, int *counts)
{
    if (head->next == NULL) // base case, end of list
        return;
    *(counts + head->data) += 1;    // increase the number by 1
    return find_counts(head->next, counts); // recalls the function on next node
}

// removes all duplicate numbers
void remove_dups(Node *start, int *counts)
{
    Node *head = start;
    if (*(counts + start->data) > 1)
    {
        Node *nodeToDelete = start;
        // If the list is empty, there is nothing to delete
        if (head == NULL){
            printf("List is empty.\n");
            return;
        }
        // If the node to delete is the first node, set the head to the next node
        if (head == nodeToDelete){
            head = (head)->next;
        }

        // If the node to delete has a previous node, set its next pointer to the node after the one to delete
        if (nodeToDelete->prev != NULL){
            nodeToDelete->prev->next = nodeToDelete->next;
        }

        // If the node to delete has a next node, set its previous pointer to the node before the one to delete
        if (nodeToDelete->next != NULL){
            nodeToDelete->next->prev = nodeToDelete->prev;
        }

        // Free the memory used by the node to delete
        free(nodeToDelete);
    }
    head = head->next;
}

// Print doubly linked list in reverse
void print_list(Node *linked)
{
    if (linked->next == NULL)   // base case, end of linked list
        return;
    printf("%d\n", linked->data);       // prints current number
    return print_list(linked->next);    // recalls function on next node
}

// Free memory of doubly linked list
void free_memory(Node *list)
{
    if (list == NULL)
        return free(list);
    free_memory(list->next);
    return free(list);
}