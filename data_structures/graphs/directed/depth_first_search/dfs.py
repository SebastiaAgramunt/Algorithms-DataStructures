from typing import List, Dict

GraphType = Dict[str, List[str]]


class Node:
    # Node == Vertex of the graph
    def __init__(self, val: str, visited: bool = False):
        self.val = val
        self.visited = visited


NodesList = Dict[str, Node]


def get_nodes(graph: GraphType) -> NodesList:
    # from a Graph calculate a dictionary of all the vertices
    # with value an object Graph initialized as visited=False
    nodes = {}
    for vertex in graph:
        nodes[vertex] = Node(vertex)
        for vertex2 in graph[vertex]:
            nodes[vertex2] = Node(vertex2)

    return nodes


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.isEmpty():
            val = self.stack[0]
            self.stack = self.stack[1:]
            return val
        return None

    def add(self, val):
        self.stack = [val] + self.stack

    def isEmpty(self):
        return False if len(self.stack) > 0 else True


def dfs(graph: GraphType, start: str) -> None:
    nodes = get_nodes(graph)
    stack = Stack()

    stack.add(start)

    while not stack.isEmpty():

        node = stack.pop()
        if not nodes[node].visited:
            nodes[node].visited = True
            for neighbor in graph[node]:
                stack.add(neighbor)
            print(f"Node {node} visited, Stack: {stack.stack}")


if __name__ == "__main__":
    graph: GraphType = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["A", "F"],
        "E": ["F"],
        "F": ["G"],
        "G": [],
        "H": ["B"],
    }

    # transverse from start_node all the graph
    # visit all nodes that you can
    start_node = "A"
    dfs(graph, start_node)
