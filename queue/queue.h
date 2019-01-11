#ifndef QUEUE_H_   /* Include guard */
#define QUEUE_H_

struct Queue{
    int front,rear,capacity;
    int* array;
    int size;
};

int IsEmpty(struct Queue*);
int IsFull(struct Queue*);
int Dequeue(struct Queue*);
void Enqueue(struct Queue*, int);
void PrintQueue(struct Queue* );
struct Queue* create_queue(int);

#endif