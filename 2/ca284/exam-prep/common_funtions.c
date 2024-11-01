typedef struct Node Node;

struct Node {
    Node *prev;
    float data;
    Node *next;
};

// failed memory allocation
if (!/*variable*/)
    memory_exit();

void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// converts command args to array
void build_array(char *argv[], int *len, float *nums)
{
    for (int i = 0; i < *len; ++i)
    {
        *(nums + i) = atof(*(argv + i + 2));
    }
}

// Build Doubly Linked List from array, return tail
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

// Print doubly linked list in reverse
void print_list(Node *linked)
{
    if (linked == NULL)
        return;
    printf("%.2f\n", linked->data);
    return print_list(linked->prev);
}

// Free memory of doubly linked list
void free_memory(Node *list)
{
    if (list == NULL)
        return free(list);
    free_memory(list->next);
    return free(list);
}

// Pop last node of linked list, using tail
Node *pop(Node *tail)
{
    tail = tail->prev;
    free(tail->next);
    tail->next = NULL;
    return tail;
}

// Push new Node onto end of linked list, using tail
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

// insert new node 'num' at position 'pos'
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