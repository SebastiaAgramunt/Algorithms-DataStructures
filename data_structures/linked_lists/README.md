# Linked List

First implementation is a [single linked list](https://en.wikipedia.org/wiki/Linked_list). The first element of the list is called head and its pointer is well determined when we declare the structure. Every element of the linked list consists of an integer (could be any other structure) and a pointer to the next element:

```c
struct Node{
    int data;
    struct Node *next;
};
```

In order to get to the Nth element we need to loop from 0 to N and therefore is a larger computation compared to an array created using calloc or malloc. In this last one getting to an arbitrary element is of order 1. Linked lists have advantages though, we can insert elements in any position without having to change the other elements in the list. Also, lists are of arbitrary lenght (your computer memory is your limit), once created you can freely add elements. That's good if you don't know a priori the lenth of you array.

Compile and execute the code as:
```
make
./llists
```
In the code we just have two ways to add elements, before the head and at the end. 