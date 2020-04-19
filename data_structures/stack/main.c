#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main()
{

    struct Stack* stack = create_stack(5);
    add_item_stack(stack,2);
    add_item_stack(stack,3);
    add_item_stack(stack,5);
    add_item_stack(stack,4);
    print_stack(stack);
    printf("\n");

    pop_item_stack(stack);
    print_stack(stack);
    printf("\n");
    return 0;
}