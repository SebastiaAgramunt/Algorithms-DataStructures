#include<stdio.h>
#include<stdlib.h>
#include "linked_lists.h"

//insert element at beginning replacing head
struct Node* InsertBegin(struct Node *head, int i){
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node));
    (*new_node).data = i;
    (*new_node).next = head;
    head = new_node;
    return head;
}

//insert element at the end. Last element next must point to NULL
void InsertEnd(struct Node *head, int i){
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node));
    (*new_node).data = i;
    (*new_node).next = NULL;

    struct Node *p = head;
    while(p != NULL)
    {
        if((*p).next == NULL)
        {
            (*p).next = new_node;
            break;
        }
        p = (*p).next;
    }
}

struct Node* DeleteElement(struct Node* head, int i){
    struct Node* p = head;
    struct Node* prev = NULL;

    //if first element is i, return head as next
    if((*p).data == i){
        return (*p).next;
    }else{
        while(p!=NULL){
            prev = p;
            p = (*p).next;
            if((*p).data == i){
                (*prev).next = (*p).next;
                return head;
            }
        }
        return(head);
    }
}

void Print(struct Node *head){
    struct Node* p = head;
    while(p!=NULL){
        printf("elem = %d, addr = %p\n",(*p).data,p);
        p = (*p).next;
    }
}
