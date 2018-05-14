## Queue Data Structure

A C structure modeling a FIFO queue of integers. The basic structure is:

```c
struct Queue{
    int front,rear,capacity;
    int* array;
    int size;
};
```
We must define two functions, enqueue and dequeue. The first one is used to add new items to the list whilst the second to remove the items in order in the list. Rear and front indicate the tail and the front of the list, respectively. 

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```