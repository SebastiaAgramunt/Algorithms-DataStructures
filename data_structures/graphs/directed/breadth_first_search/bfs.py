from typing import List, Dict

GraphType = Dict[str, List[str]]


class Node:
    # Node == Vertex of the graph
    def __init__(self, val: str, visited: bool = False):
        self.val = val
        self.visited = visited


class Queue:
    # simple queue impolementation in python
    def __init__(self):
        self.queue = []

    def add(self, val):
        self.queue.append(val)

    def pop(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            self.queue = self.queue[1:]
            return val
        return None

    def isEmpty(self):
        return True if len(self.queue) == 0 else False


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


def bfs(graph: GraphType, start: str):
    "Breadth First Search uses a Queue"
    nodes = get_nodes(graph)
    queue = Queue()

    queue.add(start)

    while not queue.isEmpty():
        s = queue.pop()
        if not nodes[s].visited:
            nodes[s].visited = True
            for neighbor in graph[s]:
                queue.add(neighbor)
            print(f"Node {s} visited, Queue: {queue.queue}")


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
    bfs(graph, start_node)
