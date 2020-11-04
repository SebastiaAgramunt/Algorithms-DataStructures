# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time


########################################################################################
## my approach is to create a stack of a class called Node. Each node contains
# the value we want to add and the maximum so far, therefore when we pop we simply
# delete one node and the maximum corresponds to the maxvalue of the following
# node element on the stack. 
# its O(1) in all operations but it requires 2N in memory where N is the size of the
# stack.

import sys
from typing import List
from random import randrange, seed

class Node:
    def __init__(self, val: int, maxval: int = None):
        self._val = val
        self._maxval = maxval

    @property
    def val(self):
        return self._val

    @property
    def maxval(self):
        return self._maxval


class Stack:
    def __init__(self):
        self._stack = []

    def stack_as_list(self):
        return [node.val for node in self._stack]

    def push(self, val: int):
        if len(self._stack) == 0:
            self._stack.append(Node(val, val))
        elif self._stack[-1].maxval < val:
            self._stack.append(Node(val, val))
        else:
            self._stack.append(Node(val, self._stack[-1].maxval))

    def pop(self):
        if len(self._stack) == 0:
            return None
        else:
            last_node = self._stack[-1]
            del self._stack[-1]
            return last_node.val

    def max(self):
        return self._stack[-1].maxval

    def __str__(self):
        if len(self._stack) > 0:
            s = "The stack is: \n"
            s += "[" + ", ".join(map(str, self.stack_as_list()))+ "]"
            s += f"\nwith maximum value: {self._stack[-1].maxval}\n"
            return s
        else:
            return ""


if __name__ == "__main__":

    seed(1)
    N = 55
    n_max = 1000

    stack = Stack()

    for _ in range(N):
        stack.push(randrange(n_max))

    print(stack)

    #pop several elements
    for _ in range(10):
        elem = stack.pop()

    print(stack)

