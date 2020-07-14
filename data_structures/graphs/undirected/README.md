# Undirected graphs

An ***undirected graph*** is a graph whose edge direction is not defined. This is the same as to say that the edges can go in both directions, i.e. if it exists ```("A", "B")``` then also exist ```("B", "A")```.

In python we can represent an undirected graph using the type ```Dict[str, List[str]]``` but it would be cumbersome, it is best represented just specifying the edges for instance using a list of tuples or an adjacency matrix (symmetric by definition).

```python
from typing import List, Tuple

UndirectedGraphType = List[Tuple[str, str]]

graph: UndirectedGraphType = [
	("A", "B"),
	("A", "C"),
	("C", "F"),
	("F", "G"),
]
```
or

```python
from typing import List
import numpy as np

keys = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

# an adjacency matrix
AdjacencyMatrixType = List[List[int]]

# a simmetric matrix with 0's and 1's indicating True False for existing edge
graph: AdjacencyMatrixType = [
	[0, 1, 0, 1, 1, 0],
	[1, 0, 0, 0, 1, 0],
	[0, 0, 0, 1, 1, 0],
	[1, 0, 1, 0, 1, 0],
	[1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0],
]
np_graph = np.array(graph, dtype=np.int)
assert np.array_equal(np_graph,np_graph.T), "Matrix is not symetric and does not represent undirected graph"

v1, v2 = "A", "D"
exist_edge = graph[keys[v1]][keys[v2]]
print(f"Does exist an edge from {v1} to {v2}? {exist_edge}")

```

As you may have notticed we can also represent a directed graph with the adjacency matrix but in this case if ```graph["A"]["B"]``` is 1, ```graph["B"]["A"]``` is 0 for every A and B nodes in the graph, otherwise we would have an undirected node.

A ***connected graph*** is a graph that has a path in between each pair of nodes. I.e. no matter what is our starting point or ending point we will find a path. A simple example of this is the graph represented by the adjacency matrix unity (all 1s) a.k.a ***complete graph***.