#ifndef LINKED_LISTS_H_   /* Include guard */
#define LINKED_LISTS_H_

struct Node{
    int data;
    struct Node *next;
};

//insert element at beginning replacing head
struct Node* InsertBegin(struct Node*, int);
//insert element at the end. Last element next must point to NULL
void InsertEnd(struct Node*, int);
void Print(struct Node*);

#endif