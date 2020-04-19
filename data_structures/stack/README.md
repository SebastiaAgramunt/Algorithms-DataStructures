## Queue Data Structure

Basic implementation of a stack data structure:

```c
struct Stack{
    int i;
    int* arr;
    int size;
};
```
Two functions have to be implemented. ```add_item_stack``` that adds an item on top of the stack and ```pop_item_stack``` that gives the last element added to the stack. 

In the example provided in the code we create a stack of size 5 and fill it with the numbers (in order) 2,3,5 and 4. Then the last element added (4) is the first to be poped out in a sequence "last in first out".