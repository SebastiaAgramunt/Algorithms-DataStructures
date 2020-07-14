# Breadth first transversal

A graph can be transversed in several ways, one of them is breadth first. In this transversal we use the **queue** data structure to keep track of the nodes.

For instance a directed graph

```python
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

is transversed (breadth wise) starting from node "A" as:

```
Node A visited, Queue: ['B', 'C']
Node B visited, Queue: ['C', 'D', 'E']
Node C visited, Queue: ['D', 'E', 'F']
Node D visited, Queue: ['E', 'F', 'A', 'F']
Node E visited, Queue: ['F', 'A', 'F', 'F']
Node F visited, Queue: ['A', 'F', 'F', 'G']
Node G visited, Queue: []
```

We start and node A whose neighbors (adjacent edges) are B and C, so we add those to the queue eliminating A. Then we explore the next element in the queue, that is B whose adjacent index are D and E and so we add them to the queue eliminating B. This process is repeated until the queue is empty. See that H is never visited because it is an isolated node.

Recall thad breadth first then means that we explore first the adjacent elements to the current node. This algorithm is useful to find the minimum length path between two nodes (minimum number of hops as this graph is unweighted).

## Shortest path

In breadth first transversal we have to keep track on which nodes we have visited not to visit them again. See that when we visit node F the queue formed is ```Node F visited, Queue: ['A', 'F', 'F', 'G']``` but nodes in the queue have already been visited exept for ```G``` which is empty. Therefore the visit sequence is ```A -> B -> C -> D -> E -> F -> G```. 

To find the minimum path we transverse breadth-wise the graph from the initial node to the final one whilst keeping track of the visited nodes. A good trick to do so is to queue the explored paths.