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


def bfs_shortest_path(graph: GraphType, start: str, stop: str):
    """Shortest path to transverse a directed graph
    Input:
        - graph: GraphType specifying the nodes and edges
        - start: a node starting point
        - stop: an end point
    Output:
        - The minimum path from start to stop
    """
    nodes = get_nodes(graph)
    queue = Queue()

    # path is a queue and first path is start
    queue.add([start])

    while not queue.isEmpty():
        # pop the first path from the queue
        path = queue.pop()
        # get the last node from the path
        node = path[-1]
        if not nodes[node].visited:
            nodes[node].visited = True
            for neighbor in graph[node]:
                # new path is the path + the neighbor
                new_path = list(path)
                new_path.append(neighbor)

                # add the path to the queue
                queue.add(new_path)

                if neighbor == stop:
                    return new_path


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

    start_node = "A"
    end_node = "G"
    shortest_path = bfs_shortest_path(graph, start_node, end_node)
    print(shortest_path)
