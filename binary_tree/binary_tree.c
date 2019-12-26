#include <stdio.h>
#include <stdlib.h>
#include "binary_tree.h"

void PrintInOrder(struct Node* node){
	if(node != NULL){
		PrintInOrder((*node).left);
		printf("%d ", (*node).val);
		PrintInOrder((*node).right);
	}
}

void PrintPostOrder(struct Node* node){
	if(node != NULL){
		PrintPostOrder((*node).left);
		PrintPostOrder((*node).right);
		printf("%d ", (*node).val);
	}
}

void PrintPreOrder(struct Node* node){
	if(node != NULL){
		printf("%d ", (*node).val);
		PrintPreOrder((*node).left);
		PrintPreOrder((*node).right);
	}
}

struct Node* NewNode(int val){
	struct Node* node = (struct Node*)malloc(sizeof(struct Node)); 
	(*node).val = val;

	(*node).left = NULL;
	(*node).right = NULL;

	return(node);
}