# Given a list of integers S and a target number k, write a function that returns a 
# subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers 
# in the list are positive. For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, 
# return [12, 9, 2, 1] since it sums up to 24.


# This is an NP-hard problem... used in crypto. We will follow a strategy for a graph
# search, first what we need to do is to sort the list:

from typing import List
from copy import deepcopy
from random import seed, randrange

class Node:
    def __init__(self, l: List[int], visited: List[int]=[]):
        self.l = deepcopy(l)
        self.visited = deepcopy(visited)

    def sum(self):
        return sum(self.visited)

    def _expand_helper(self, i: int):
        if i<len(self.l):
            l = deepcopy(self.l)
            visited = deepcopy(self.visited)
            visited.append(l[i])
            del l[i]

            return Node(l, visited)

    def expand(self):
        if len(self.l)==0:
            nodes = []
        else:
            nodes = [self._expand_helper(i) for i in range(len(self.l))]
        return nodes


# explore in a depth first search
class Stack:
    def __init__(self, nodes: List[Node], target: int):
        self.nodes = nodes
        self._target = target

    def explore(self):
        while len(self.nodes)>0:
            node = self.nodes.pop()
            child_nodes = node.expand()

            for child_node in child_nodes:
                s = child_node.sum()
                if s == self._target:
                    return child_node.visited
                elif s < self._target:
                    self.nodes.append(deepcopy(child_node))

        return []


if __name__ == "__main__":
    #l = [12, 1, 61, 5, 9, 2]
    #target = 24
    n = 100
    max_i = n//4

    l = [randrange(max_i) for _ in range(n)]
    target = randrange(5*n)

    root = Node(l)
    stack = Stack([root], target)

    result = stack.explore()
    print(f"Sublist is: {result}\nsumming {sum(result)}")


    assert sum(result) == target, "Algorithm is not correclty implemented"


