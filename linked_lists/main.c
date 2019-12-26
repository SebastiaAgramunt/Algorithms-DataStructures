#include<stdio.h>
#include<stdlib.h>
#include "linked_lists.h"

int main()
{

    struct Node *first = (struct Node*)malloc(sizeof(struct Node));
    struct Node *second = (struct Node*)malloc(sizeof(struct Node));
    struct Node *third = (struct Node*)malloc(sizeof(struct Node));

    (*first).data = 0;
    (*first).next = second;

    (*second).data = 1;
    (*second).next = third;

    (*third).data = 2;
    (*third).next = NULL;

    struct Node* head= first; //first node is the head

    printf("Original linked list: \n");
    Print(head);
    head = InsertBegin(head,10);
    InsertEnd(head,50);

    printf("After inserting two elements: \n");
    Print(head);

    printf("Deleting element 0: \n");
    head = DeleteElement(head, 0);
    Print(head);

    return 0;
}