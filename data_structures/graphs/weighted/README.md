# Weighted graphs

Weighed graphs is another kind of graphs in which the edges contain a value (a real number). This kind of graphs make sense when defining distances, e.g. I may have a road going from Barcelona to Madrid (an edge) and another from Barcelona to Paris, in an unweighted graph we are just saying that there is a road and not what is the distance between the cities.

In my opinion best way to represent weighted graphs is through the adjacency matrix

```python
from typing import List
import numpy as np

keys = {"Barcelona": 0, "Paris": 1, "Bilbao": 2, "Santiago de Compostela": 3, "New York": 5}

# an adjacency matrix
AdjacencyMatrixType = List[List[int]]

# an undirected graph (highways are two way)
graph: AdjacencyMatrixType = [
	[0, 1039, 609, 1089, None],
	[1039, 0, 920, 1495, None],
	[609, 920, 0, 581, None],
	[1089, 1495, 581, 0, None],
	[None, None, None, None, 0],
]

v1, v2 = "Barcelona", "Bilbao"
distance_km = graph[keys[v1]][keys[v2]]
print(f"Distance from {v1} to {v2}? {distance_km}")

```
In the above example New York is an isolated node, from New York we can only go to New york and with cost 0, there is no road from New York to all the other defined cities.

This kind of graph opens new problems to solve, like finding the minimum travel distance between two cities (what happens if two cities are not directly connected, what itinerary of cities we should follow to connect those?). Another important problem here is the so called traveling salesman problem, that is formulated as follows:

*A salesman has to visit N clients that are scattered on a large city. In which order has to visit the salesman all the clients so that the distance travelled is minimum?*

Simple, right?. It turns out to be extremely complex to solve as N increases. We will see an example in the code. 