#ifndef BINARY_TREE_   /* Include guard */
#define BINARY_TREE_

struct Node{
	int val;
	struct Node* left;
	struct Node* right;
};

void PrintInOrder(struct Node*);
void PrintPostOrder(struct Node*);
void PrintPreOrder(struct Node*);
struct Node* NewNode(int);

#endif