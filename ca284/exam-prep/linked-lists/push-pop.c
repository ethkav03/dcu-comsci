#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
    Node *prev;
    int data;
    Node *next;
};

void build_array(char *argv[], int *len, int *nums);
Node *build_list(int *nums, int *n, Node *linked, int i, Node *prev);
void print_list(Node *linked);
Node *pop(Node *tail);
Node *push(Node *tail, int n);

int main(int argc, char *argv[])
{
    int *n = malloc(sizeof(int));
    *n = atoi(argv[1]);

    int *nums = calloc(*n, sizeof(int));
    build_array(argv, n, nums);

    Node *linked = malloc(sizeof(Node));

    Node *tail = malloc(sizeof(Node));
    tail = build_list(nums, n, linked, 0, NULL);

    //print_list(tail);

    tail = pop(tail);
    tail = pop(tail);

    tail = push(tail, atoi(argv[argc - 2]));
    tail = push(tail, atoi(argv[argc - 1]));

    print_list(linked);
}

void build_array(char *argv[], int *len, int *nums)
{
    for (int i = 0; i < *len; ++i)
    {
        *(nums + i) = atoi(*(argv + i + 2));
    }
}

Node *build_list(int *nums, int *n, Node *linked, int i, Node *prev)
{
    if (i == *n - 1)
    {
        linked->prev = prev;
        linked->data = *(nums + i);
        linked->next = NULL;
        return linked;
    }
    linked->prev = prev;
    linked->data = *(nums + i);
    linked->next = malloc(sizeof(Node));
    return build_list(nums, n, linked->next, i + 1, linked);
}

void print_list(Node *linked)
{
    if (linked == NULL)
        return;
    printf("%d\n", linked->data);
    return print_list(linked->next);
}

Node *pop(Node *tail)
{
    tail = tail->prev;
    free(tail->next);
    tail->next = NULL;
    return tail;
}

Node *push(Node *tail, int n)
{
    Node *curr = tail;
    curr->next = malloc(sizeof(Node));
    curr = curr->next;
    curr->prev = tail;
    curr->data = n;
    curr->next = NULL;
    return curr;
}