#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
    int data;
    Node *next;
};

void build_array(char *argv[], int *len, int *nums);
void build_list(int *nums, int *n, Node *linked, int i);
void print_list(Node *linked);

int main(int argc, char *argv[])
{
    int *n = malloc(sizeof(int));
    *n = atoi(argv[1]);

    int *nums = calloc(*n, sizeof(int));
    build_array(argv, n, nums);

    Node *linked = malloc(sizeof(Node));
    build_list(nums, n, linked, 0);

    print_list(linked);
}

void build_array(char *argv[], int *len, int *nums)
{
    for (int i = 0; i < *len; ++i)
    {
        *(nums + i) = atoi(*(argv + i + 2));
    }
}

void build_list(int *nums, int *n, Node *linked, int i)
{
    if (i == *n)
    {
        linked = NULL;
        return;
    }
    linked->data = *(nums + i);
    linked->next = malloc(sizeof(Node));
    return build_list(nums, n, linked->next, i + 1);
}

void print_list(Node *linked)
{
    if (linked->next == NULL)
        return;
    printf("%d\n", linked->data);
    return print_list(linked->next);
}