# Graphs

A graph is a mathematical object consisting on nodes (or vertices) and edges.

* **Node**: An entity, can be an object, a string, a concept, an integer or whatever you may think.
* **Edge**: Describes the relationship between two nodes. An edge or ordered pair is a connection between two nodes u,v that is identified by unique pair(u,v). The pair (u,v) is ordered because (u,v) is not same as (v,u).

An example of graph can be the following (written in python syntax)

```python
from typing import List, Dict

GraphType = Dict[str, List[str]]

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
```

The nodes are the letters "A", "B", ... "H" and the edges are described by the list of nodes contained on each key in the dictionary. For instance:

```A: ["B", "C"]``` describes the edges of ```A```, here from ```A``` we can go to nodes ```B``` and ```C``` and not necessarily vice-versa. In the notation above for edges, this relationship gives us the nodes ("A", "B") and ("A", "C").

Other entities worth mentioning on graphs are the path and the ajacency matrix:

* **Path**: A path of length ```N``` from node ```A``` to node ```B``` is defined as sequence of ```N+1``` nodes ```P(A, B) = [V0, V1, ..., VN]```. There can be cases where there's no path between two nodes, for instance in the above example there is no way to go from ```A``` to ```H``` since no node goes to ```H``` but it is easy to construct a path from ```A``` to ```B``` and takes just one step. The lenght of the path is called the distance of the path.

* **Adjacency matrix**: A matrix that describes the connection between two nodes. if there are ```N``` nodes such matrix will be of size ```NxN``` and will be filled with 1's when there's an edge between the nodes and a 0 otherwise (more on that later). 
