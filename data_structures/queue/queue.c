#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

struct Queue* create_queue(int capacity){
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    (*queue).front = 0; //index to remove items
    (*queue).rear = capacity -1;
    (*queue).capacity = capacity;
    (*queue).size = 0;
    (*queue).array = (int*)malloc(capacity*sizeof(int));

    return queue;
}

int IsEmpty(struct Queue* queue){
    return (*queue).size == 0;
}
int IsFull(struct Queue* queue){
    return (*queue).size == (*queue).capacity;
}

//pop items from the queue folloing FIFO
int Dequeue(struct Queue* queue){
    if(IsEmpty(queue)){
        return 0;
    }

    int item = (*queue).array[(*queue).front];
    (*queue).front = ((*queue).front + 1)%(*queue).capacity;
    (*queue).size -=1;
    return item;
}

//add items to the queue
void Enqueue(struct Queue* queue, int item){
    if(IsFull(queue)){
        return;
    }
    (*queue).size +=1;
    (*queue).rear = ((*queue).rear + 1)%(*queue).capacity;
    (*queue).array[(*queue).rear] = item;
}

void PrintQueue(struct Queue* queue){
    for(int i = (*queue).front; i < (*queue).rear+1; i++){
        printf("%d\n", (*queue).array[i]);
    }
}
