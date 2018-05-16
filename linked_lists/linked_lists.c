#include<stdio.h>
#include<stdlib.h>

//Node in a single linked list, points to the next element
struct Node{
    int data;
    struct Node *next;
};

//insert element at beginning replacing head
struct Node* InsertBegin(struct Node *head, int i)
{
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node));
    (*new_node).data = i;
    (*new_node).next = head;
    head = new_node;
    return head;
}

//insert element at the end. Last element next must point to NULL
void InsertEnd(struct Node *head, int i)
{
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

void Print(struct Node *head){
    struct Node* p = head;
    while(p!=NULL){
        printf("elem = %d, addr = %p\n",(*p).data,p);
        p = (*p).next;
    }
}


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

    return 0;
}