#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node {
    Node *prev;
    int data;
    Node *next;
};

Node *build_list(int *nums, int n, Node *linked, int i, Node *prev);
void print_list(Node *linked);
void insert(Node *list, int num, int pos);

int main(int argc, char *argv[])
{
    int numbers[] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};
    int *nums = &numbers[0];

    Node *linked = malloc(sizeof(Node));

    Node *tail = malloc(sizeof(Node));
    tail = build_list(nums, 10, linked, 0, NULL);

    int num = atoi(argv[argc - 1]);
    int pos = atoi(argv[argc - 2]);

    insert(linked, num, pos);

    print_list(linked);
}

Node *build_list(int *nums, int n, Node *linked, int i, Node *prev)
{
    if (i == n - 1)
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

void insert(Node *list, int num, int pos)
{
    if (list == NULL)
    {
        return;
    }
    else if (list->data == pos)
    {
        Node *new = malloc(sizeof(Node));
        new->prev = list;
        new->data = num;
        
        Node *next = list->next;
        new->next = next;
        list->next = new;
        return;
    }
    return insert(list->next, num, pos);
}