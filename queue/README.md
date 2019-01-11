## Queue Data Structure

A C structure modeling a FIFO queue of integers. The basic structure is:

```c
struct Queue{
    int front,rear,capacity;
    int* array;
    int size;
};
```
We must define two functions, enqueue and dequeue. The first one is used to add new items to the list whilst the second to remove the items in order in the list. Rear and front indicate the index for inserting elements and dequeuing elements, respectively. I.e. when we enqueue a new element, we do it by increasing rear index. We choose to enqueue by the largest index (capacity -1).

The structure defines the front, rear and the capacity of our queue. The integer elements of the queue are defined in a pointer to integer and the size is an integer that increases or decreases as we enqueue or dequeue elements.

In the example we create a queue of 7 integer elements and we start adding from 0 until 6 then we make two dequeues (remove firts two elements) and we wind up with the queue from 2 to 6. 