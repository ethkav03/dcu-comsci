/*
Author: Ethan Kavanagh
Date: 13/12/2022
Description: Takes in a paragraph and outputs the longest or shortest sentence, depending which is chosen.
Approach: Loop throught the paragraph to find the sentences and store them in structs (stores sentence and its length).
    Depending on which the user has requested, find the length of the shortest or longest sentence. Then searchs the
    doubly linked list of sentences to find the specifc sentence and then prints it.
*/

/* include libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* class definitions */
typedef struct Sentence Sentence;

struct Sentence {       // struct defining the Sentence doubly linked list
    Sentence *prev;
    char sentence[200];
    int len;
    Sentence *next;
};


/* function prototypes */
void memory_exit();
Sentence *find_sentences(char *string);
void find_longest(Sentence *curr, int *longest);
void find_shortest(Sentence *curr, int *shortest);
void print_result(Sentence *head, int *n);
void free_memory(Sentence *list);

/* main function */
int main(int argc, char* argv[])
{
    char *s = argv[1];      // the paragraph
    char *est = argv[2];    // longest or shortest

    char *result = malloc(sizeof(char*));   // allocates memory for result
    if (!result)                // checks for memory allocation error
        memory_exit();          // calls memory allocation failure function

    Sentence *head = find_sentences(s); // calls functions to find sentences and assigns reference to head of doubly linked list to head

    if (strcmp(est, "longest") == 0)        // checks for shortest or longest
    {
        int *longest = malloc(sizeof(int)); // allocates memory for longest
        if (!longest)           // checks for memory allocation error
            memory_exit();          // calls memory allocation failure function
        *longest = 0;
        find_longest(head, longest);    // calls function to find longest sentence
        print_result(head, longest);    // prints longest sentence
        free(longest);   //frees longest
    }
    else if (strcmp(est, "shortest") == 0)
    {
        int *shortest = malloc(sizeof(int));    // allocates memory for longest
        if (!shortest)                  // checks for memory allocation error
            memory_exit();          // calls memory allocation failure function
        *shortest = head->len;
        find_shortest(head, shortest);  // calls function to find shortest sentence
        print_result(head, shortest);   // // prints shortest sentence
        free(shortest);     // frees shortest
    }
    else
    {
        printf("Not valid!\n");     // if neither longest or shortest
    }

    free_memory(head);  // frees doubly linked list

    return 0;
}

/* full implementations of functions */

// failed memory allocation
void memory_exit()
{
    printf("Could not allocate memory.\n");
    exit(0);
}

// function to find sentences and add to doubly linked list
Sentence *find_sentences(char *string)
{
    int qoute = 0;      // sets qoutations to false
    Sentence *first = malloc(sizeof(Sentence)); // alocates memory for first sentence
    Sentence *curr = first; // new Sentence curr set equal to first
    if (!curr)  	        // checks for memory allocation error
        memory_exit();          // calls memory allocation failure function
    curr->prev = NULL;      // sets head prev to NULL
    int j = 0;              // increment through sentence of sentence
    for (int i = 0; i < strlen(string); ++i)    // loop through paragraph
    {

        if ((*(string + i) != '.' && *(string + i) != '!' && *(string + i) != '?')) // while no single qoutation
        {
            *(curr->sentence + j) = *(string + i);  // add current char to curr sentence
            j += 1;             // increment j by 1
            if (qoute == 0 && *(string + i) == '\'')    // if single quote encountered, toggle qoute to 1
                qoute = 1;
            else if (qoute == 1 && *(string + i) == '\'')   // if qoute is 1, and we encounter a 2nd single qoute, toggle qoute back to 0
                qoute = 0;
        }
        else if (qoute == 1 && (*(string + i) == '.' || *(string + i) == '!' || *(string + i) != '?'))  // if qoute is 1, sentence ending punctuation is added to sentence
        {
            *(curr->sentence + j) = *(string + i);  // assign value of string[i] to sentences sentence[j]
            j += 1;
        }
        else if (qoute == 0 )   // if qoute is 0
        {
            *(curr->sentence + j) = *(string + i);  // add string[i] to sentences sentence
            curr->len = strlen(curr->sentence);     // assign length of that string to current length
            Sentence *prev = curr;                  // set previous to current
            curr->next = malloc(sizeof(Sentence));  // create new sentence in current next
            curr = curr->next;                      // move on to next sentence
            curr->prev = prev;                      // assign previous node to current nodes prev
            j = 0;                                  // reset j
            i += 1;                                 // increment i
        }
    }
    curr = NULL;                        // set current to NULL, end of list
    return first;               // return head
}

// function to find longest sentence
void find_longest(Sentence *curr, int *longest)
{
    if (curr->next == NULL) // base case, end of list
        return;
    if (curr->len > *longest)   // if current length is longer than longest length, overwrite longest
        *longest = curr->len;
    return find_longest(curr->next, longest);   // recall the function on next sentence
}

// function to find shortest sentence
void find_shortest(Sentence *curr, int *shortest)
{
    if (curr->next == NULL) // base case, end of list
        return;
    if (curr->len < *shortest)  // if current length is short than shortest length, overwrite shortest
        *shortest = curr->len;
    return find_shortest(curr->next, shortest); // recall the function on next sentence
}

void print_result(Sentence *head, int *n)
{
    if (head == NULL)
    {
        return; // base case, end of list
    }
    else if (head->len == *n)   // current length is equal to result sentence
    {
        printf("%d\n", *n);     // print length
        printf("%s\n", head->sentence); // print sentence
        return;
    }
    return print_result(head->next, n); // recall the function on next sentence
}

// Free memory of doubly linked list
void free_memory(Sentence *list)
{
    if (list == NULL)
        return free(list);  // base case, end of list
    free_memory(list->next);    // recall function on next sentence
    return free(list);  // free current sentence
}