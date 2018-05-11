#include <stdio.h>
#include <stdlib.h>

struct Stack{
    int i;
    int* arr;
    int size;
};

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
        for(int k = 0; k< (*stack).i; k++){
            printf("%d\n", (*stack).arr[k]);
        }
    }
}

int main()
{

    struct Stack* stack = create_stack(5);
    add_item_stack(stack,2);
    add_item_stack(stack,3);
    add_item_stack(stack,5);
    add_item_stack(stack,4);
    print_stack(stack);
    printf("\n");

    pop_item_stack(stack);
    print_stack(stack);
    printf("\n");
    return 0;
}
