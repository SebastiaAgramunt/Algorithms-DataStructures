#include <stdio.h>
#include <stdlib.h>

struct Queue{
    int front,rear,capacity;
    int* array;
    int size;
};

struct Queue* create_queue(int capacity){
    struct Queue* queue = (struct Queue*)malloc(capacity*sizeof(struct Queue));
    (*queue).front = 0; //index to remove items
    (*queue).rear = 0; //index to add items
    (*queue).capacity = capacity;
    (*queue).size = 0;
    (*queue).array = (int*)malloc(capacity*sizeof(int));

    return queue;
}

int pop_item_queue(struct Queue* queue){
    if((*queue).size > 0){
        int item = (*queue).array[(*queue).front];
        (*queue).front = ((*queue).front + 1)%(*queue).capacity;
        (*queue).size -=1;
        return item;
    }
    else{
        return 0;
    }
}

void add_item_queue(struct Queue* queue, int item){
    if((*queue).size < (*queue).capacity){
        (*queue).array[(*queue).rear] = item;
        (*queue).size +=1;
        (*queue).rear = ((*queue).rear + 1)%(*queue).capacity;
    }
}

void print_queue(struct Queue* queue){
    for(int i = (*queue).front; i < (*queue).rear; i++){
        printf("%d\n", (*queue).array[i]);
    }
}

int main(){

    struct Queue* queue = create_queue(7);
    add_item_queue(queue,0);
    add_item_queue(queue,1);
    add_item_queue(queue,2);
    add_item_queue(queue,3);
    add_item_queue(queue,4);
    add_item_queue(queue,5);
    print_queue(queue);
    printf("\n");

    pop_item_queue(queue);
    print_queue(queue);
    printf("\n");

    return 0;
}
