# Depth first transversal

A graph can be transversed in several ways, one of them is depth first. In this transversal we use the **stack** data structure to keep track of the nodes.

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

results in the following transversal when we start from "A": 

```
Node A visited, Stack: ['C', 'B']
Node C visited, Stack: ['F', 'B']
Node F visited, Stack: ['G', 'B']
Node G visited, Stack: ['B']
Node B visited, Stack: ['E', 'D']
Node E visited, Stack: ['F', 'D']
Node D visited, Stack: ['F', 'A']
```

This is, first we visit node A that has as neighbors B and C, those are added to the stack, first B and then C creating the list [C, B]. Then we pop C that has neighbor F, and we add it to the stack, now we have [F, B]. We pop and explore F, having neighbor G and we add it to the stack [G, B] and so on... Recall that in this approach the last we see is the first we explore, this is why is called depth first as we go deeper and deeper into the graph structure.

As in the case of BFS we can decide to stop the transverse once we find the node we are interested in. However DFS does not guarantee that the path found in between two nodes is the minium one.

## Utility of depth first transversal

Depth first search is commonly used in gaming when an AI agent has a lot of multiple choices. In this case the breadth of the graph is very large and you don't get to see a lot of steps into the depth of it. Therefore a good approach is to use depth first.

Depth fist can also be used when finding paths, we will see this on weighted graphs in the case of ***best first search*** that is a modification of DFS.

## When to use DFS vs BFS

Based on a post from [stackoverflow](https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf):

* If you know a solution is not far from the root of the tree, a breadth first search (BFS) might be better.
* If the tree is very deep and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.

* If the tree is very wide, a BFS might need too much memory, so it might be completely impractical.

* If solutions are frequent but located deep in the tree, BFS could be impractical.

* If the search tree is very deep you will need to restrict the search depth for depth first search (DFS), anyway (for example with iterative deepening).