#include <stdio.h>
#include <stdlib.h>
#include "binary_tree.h"

int main(void){
    
    struct Node* head = NewNode(0);
    struct Node* first = NewNode(1);
    struct Node* second = NewNode(2);
    struct Node* third = NewNode(3);
    struct Node* fourth = NewNode(4);
    struct Node* fifth = NewNode(5);
    struct Node* sixth = NewNode(6);

    (*head).left = first;
    (*head).right = second;

    (*first).left = third;
    (*first).right = fourth;

    (*second).left = fifth;
    (*second).right = sixth;

    printf("Printing In Order\n");
    PrintInOrder(head);

    printf("\n\nPrinting Post Order\n");
    PrintPostOrder(head);

    printf("\n\nPrinting Pre Order\n");
    PrintPreOrder(head);
    
	return 0;
}