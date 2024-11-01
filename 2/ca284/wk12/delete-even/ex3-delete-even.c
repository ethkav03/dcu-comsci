//* Includes */
#include<stdio.h>
#include<stdlib.h>

/* Structure type definition */
typedef struct Node Node;

/* Structure declaration */
struct Node{
    int value;
    Node *next;
    Node *prev;
};

/* Function Prototypes */
Node *createList(char *argv[], int *pLength);
void traverList(Node *start);
void findEven(Node *start);
void  deleteFirstNode(Node *p);
void deleteLastNode();
void deleteAnyNode();

int checkEven(int value);

void printList(Node *start);

int main(int argc, char *argv[])
{
    int length = argc -1; // Number of ints
    int *pLength = &length;
        /* Make sure the input is correct. Conditions:
        1- At least one argument*/
        if (*pLength == 0)
        {   
            printf("ERROR: The program requiers at least one integer.\n");
            exit(0);
        }
    /* Declaring variables */
    Node *start = NULL;
    start = createList(argv, pLength);

    findEven(start); // Call function to remove all even numbers

    printList(start);

        /* Call functions */

        /* Release memory */

        return 0;
}

/* Function implementation */
Node *createList(char *argv[], int *pLength)
{
    Node *current, *first, *prev; // declare 3 pointers
    first = (Node*)calloc(1, sizeof(Node)); // Create the first node
    current = first; // current is the first node as well
    
    /* Allocating the first node */
    current->value = atoi(*(argv + 1));
    current->prev = NULL;
    
    /* Create the rest of the nodes */
    for (int i=1; i < *pLength; ++i)
    {
        /* Allocate the new node */
        current->next = (Node*)calloc(1, sizeof(Node));
        prev = current; // Get the previous node before moving pointer
        current = current->next; // Move the pointer to next node

        current->value = atoi(*(argv + i + 1)); // Store value
        current->prev = prev;
    }
    current->next = NULL; // In case it is the last node
    return first; // Pass reference to the first Node
}

void findEven(Node *start)
{
    Node *p = start;
    Node *tmp = NULL;

    while (p)
    {
        if (p->prev == NULL){
            deleteFirstNode(p);
        }
        else{
            p = p->next;
        }
    }
}
void deleteFirstNode(Node *p)
{
    Node *delete;
    delete = p;
    p = p->next;
    p->prev = NULL;
    //free(delete);
}

int checkEven(int value)
{
    if (value % 2 == 0){
        return 0;
    }
    return 1;
}

void printList(Node *start)
{
    Node *p = start;
    while (p)
    {
        printf("%d\n", p->value);
        p = p->next;
    }
}