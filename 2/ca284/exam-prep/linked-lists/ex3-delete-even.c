#include <stdio.h>
#include <stdlib.h>

// Node of a doubly-linked list
struct Node {
  int data;
  struct Node* prev;
  struct Node* next;
};

// Function to create a new node with given data
struct Node* newNode(int data)
{
  // Allocate memory for the new node
  struct Node* node = (struct Node*) malloc(sizeof(struct Node));

  // Set the data of the node
  node->data = data;

  // Set the prev and next pointers of the node to NULL
  node->prev = NULL;
  node->next = NULL;

  return node;
}

// Function to insert a new node at the beginning of the list
void push(struct Node** head, int data)
{
  // Create a new node
  struct Node* node = newNode(data);

  // If the list is empty, set the new node as the head
  if (*head == NULL) {
    *head = node;
    return;
  }

  // Otherwise, set the new node as the head and update the pointers
  node->next = *head;
  (*head)->prev = node;
  *head = node;
}

// Function to find and delete all even numbers from the list
void deleteEven(struct Node** head)
{
  // Pointer to traverse the list
  struct Node* curr = *head;

  // Loop through the list until we reach the end
  while (curr != NULL) {
    // If the current node has an even number, delete it
    if (curr->data % 2 == 0) {
      // Store a pointer to the next node
      struct Node* next = curr->next;

      // If the current node is the head, set the next node as the head
      if (curr == *head) {
        *head = next;
        if (next != NULL)
          next->prev = NULL;
      }
      else {
        // Otherwise, update the prev and next pointers of the neighboring nodes
        curr->prev->next = next;
        if (next != NULL)
          next->prev = curr->prev;
      }

      // Free the memory of the current node
      free(curr);

      // Set the current node to the next node
      curr = next;
    }
    else {
      // Move to the next node
      curr = curr->next;
    }
  }
}

// Function to calculate the sum of all odd numbers in the list
int sumOdd(struct Node* head)
{
  // Variable to store the sum
  int sum = 0;

  // Pointer to traverse the list
  struct Node* curr = head;

  // Loop through the list and sum the odd numbers
  while (curr != NULL) {
    if (curr->data % 2 == 1)
      sum += curr->data;
    curr = curr->next;
  }

  return sum;
}

// Function to display the elements of the list
void display(struct Node* head)
{
  // Pointer to traverse the list
  while (head != NULL)
  {
    printf("%d\n", head->data);
    head = head->next;
  }
}