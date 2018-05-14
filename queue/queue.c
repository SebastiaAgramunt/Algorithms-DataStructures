#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct Queue{
    int front,rear,capacity;
    int* array;
    int size;
};

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

int Dequeue(struct Queue* queue){
    if(IsEmpty(queue)){
        return INT_MAX;
    }

    int item = (*queue).array[(*queue).front];
    (*queue).front = ((*queue).front + 1)%(*queue).capacity;
    (*queue).size -=1;
    return item;
}

void Enqueue(struct Queue* queue, int item){
    if(IsFull(queue)){
        printf("blaaaa");
        return;
    }
    //printf("item %d,%d,%d\n",item,(*queue).size,(*queue).rear);
    (*queue).size +=1;
    (*queue).rear = ((*queue).rear + 1)%(*queue).capacity;
    (*queue).array[(*queue).rear] = item;
    //printf("item %d,%d,%d\n",item,(*queue).size,(*queue).rear);
    //printf("%d enqueued to queue\n", item);
}

void PrintQueue(struct Queue* queue){
    for(int i = (*queue).front; i < (*queue).rear+1; i++){
        printf("%d\n", (*queue).array[i]);
    }
}

int main(){

    struct Queue* queue = create_queue(7);
    Enqueue(queue,0);
    Enqueue(queue,1);
    Enqueue(queue,2);
    Enqueue(queue,3);
    Enqueue(queue,4);
    Enqueue(queue,5);
    Enqueue(queue,6); 
    
    printf("Queue:");
    PrintQueue(queue);
    printf("\n");

    Dequeue(queue);
    Dequeue(queue);

    printf("Queue after 2 dequeues:");
    PrintQueue(queue);
    printf("\n");

    return 0;
}
