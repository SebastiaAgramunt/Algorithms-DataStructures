#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

struct Stack* create_stack(int size){
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    (*stack).i = -1;
    (*stack).arr = (int *)malloc(size*sizeof(int));
    (*stack).size = size;
    return stack;
}

void add_item_stack(struct Stack* stack, int item){
    if((*stack).i+1 < (*stack).size){
        (*stack).i+=1;
        (*stack).arr[(*stack).i] = item; 
    }
}

int pop_item_stack(struct Stack* stack){
    if((*stack).i > 0){
        (*stack).i -=1;
        return (*stack).arr[(*stack).i + 1];
    }
    else{
        return 0;
    }
}

void print_stack(struct Stack* stack){
    if((*stack).i > 0){
        for(int k = 0; k< (*stack).i+1; k++){
            printf("%d\n", (*stack).arr[k]);
        }
    }
}

