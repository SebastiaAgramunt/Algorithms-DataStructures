#ifndef STACK_H_   /* Include guard */
#define STACK_H_

struct Stack{
    int i;
    int* arr;
    int size;
};

struct Stack* create_stack(int);
void add_item_stack(struct Stack*, int);
int pop_item_stack(struct Stack*);
void print_stack(struct Stack*);

#endif // FOO_H_