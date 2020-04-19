#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

int main(){

    struct Queue* queue = create_queue(7);
    Enqueue(queue,0);
    Enqueue(queue,1);
    Enqueue(queue,2);
    Enqueue(queue,3);
    Enqueue(queue,4);
    Enqueue(queue,5);
    Enqueue(queue,6); 
    
    printf("Queue:\n");
    PrintQueue(queue);
    printf("\n");

    Dequeue(queue);
    Dequeue(queue);

    printf("Queue after 2 dequeues:\n");
    PrintQueue(queue);
    printf("\n");

    return 0;
}