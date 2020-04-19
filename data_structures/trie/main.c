#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <stdbool.h> 

#define ALPHABET_SIZE 26 

int char_to_index(char c){
	return ((int)c - (int)'a');
}

struct Node{
	struct Node **children; //pointer to pointer containing a new son node
	bool endOfWord;
	char letter;
	int counter;
};

struct Node* createNode(void){
	struct Node* node = (struct Node*)malloc(sizeof(struct Node));

	(*node).children = (struct Node**)malloc(ALPHABET_SIZE*sizeof(struct Node*));
	for(int i=0; i<ALPHABET_SIZE;i++){
		(*node).children[i] = NULL;
	}
	(*node).endOfWord = false;
	(*node).counter = 0;

	return node;
}

void insertWord(struct Node* root,char *word){

	struct Node* ptr = root;
	int N = strlen(word);
	for(int i=0; i<N; i++){
		int letter_i = char_to_index(word[i]);
		if((*ptr).children[letter_i]==NULL){

			(*ptr).children[letter_i] = createNode();
			(*ptr).letter = word[i];
			(*ptr).counter+=1;

		}else{
			(*ptr).counter+=1;
		}
		ptr = (*ptr).children[letter_i];
	}
	(*ptr).endOfWord = true;
}

bool search(struct Node* root, char *word){
	struct Node* ptr = root;
	int N = strlen(word);

	for(int i=0; i<N; i++){
		int letter_i = char_to_index(word[i]);
		if((*ptr).children[letter_i]==NULL){
			return false;
		}
		ptr = (*ptr).children[letter_i];
	}
	return (*ptr).endOfWord;
}


int main(){

  	struct Node* head = createNode();
  	insertWord(head, "the");
  	insertWord(head, "a");
  	insertWord(head, "there");
  	insertWord(head, "answer");
  	insertWord(head, "any");
  	insertWord(head, "by");
  	insertWord(head, "bye");
  	insertWord(head, "their");

  	char word[8] = "the";
  	printf("Is 'the' in the trie? %d\n", search(head, word));

  	char word2[8] = "byes";
  	printf("Is 'byes' in the trie? %d\n", search(head, word2));

  	char word3[8] = "aswe";
  	printf("Is 'aswe' in the trie? %d\n", search(head, word3));

  	char word4[8] = "their";
  	printf("Is 'their' in the trie? %d\n", search(head, word4));


}