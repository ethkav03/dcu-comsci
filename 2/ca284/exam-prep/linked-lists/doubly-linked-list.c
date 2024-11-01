#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
    Node *prev;
    float data;
    Node *next;
};

void build_array(char *argv[], int *len, float *nums);
Node *build_list(float *nums, int *n, Node *linked, int i, Node *prev);
void print_list(Node *linked);

int main(int argc, char *argv[])
{
    int *n = malloc(sizeof(int));
    *n = atoi(argv[1]);

    float *nums = calloc(*n, sizeof(float));
    build_array(argv, n, nums);

    Node *linked = malloc(sizeof(Node));

    Node *tail = malloc(sizeof(Node));
    tail = build_list(nums, n, linked, 0, NULL);

    print_list(tail);

    free_memory(linked);

    print_list(tail);
}

void build_array(char *argv[], int *len, float *nums)
{
    for (int i = 0; i < *len; ++i)
    {
        *(nums + i) = atof(*(argv + i + 2));
    }
}

Node *build_list(float *nums, int *n, Node *linked, int i, Node *prev)
{
    if (i == *n)
    {
        linked = NULL;
        return prev;
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
    printf("%.2f\n", linked->data);
    return print_list(linked->prev);
}

void free_memory(Node *list)
{
    if (list == NULL)
        return free(list);
    free_memory(list->next);
    return free(list);
}