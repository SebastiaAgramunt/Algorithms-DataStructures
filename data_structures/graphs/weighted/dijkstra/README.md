# Dijkstra search

Dijkstra search is an algorithm that can be applied on a weighted graph with all the weights positive but not necessarily an undirected graph. It is an algoirthm that assures us that we will find the shortest path in between two nodes, however it is very computational expensive.


## How Dijkstra works?

Let's assume we have 10 cities named from A to J and we want to find the minimum path from J to F, of course having the adjacency matrix which for now will consider a symmetric matrix (i.e. undirected graph).

```
adjacency matrix: [
    [0, 2937, 4342, 3814, 2040, 1284, 3842, 779, 4701, 1775]
    [2937, 0, 1491, 1568, 589, 3644, 14, 10, 1765, 339]
    [4342, 1491, 0, 592, 1629, 1677, 1612, 784, 2958, 1193]
    [3814, 1568, 592, 0, 2718, 4940, 4882, 2768, 2911, 984]
    [2040, 589, 1629, 2718, 0, 1513, 1442, 187, 732, 37]
    [1284, 3644, 1677, 4940, 1513, 0, 3431, 4739, 927, 1482]
    [3842, 14, 1612, 4882, 1442, 3431, 0, 1609, 2015, 946]
    [779, 10, 784, 2768, 187, 4739, 1609, 0, 2906, 513]
    [4701, 1765, 2958, 2911, 732, 927, 2015, 2906, 0, 885]
    [1775, 339, 1193, 984, 37, 1482, 946, 513, 885, 0]
    ]
```

We consider the paths as the city visited and the cost (distance, travel time etc...) from J to that city. For instance 

```
Path = [('J', 0), ('E', 37), ('H', 224), ('B', 234), ('G', 248)]
```

means that we went from J to E having a cost 37 (have a look at the adjacency matrix), then from E to H that has a cost of 187, therefore adding up to 224. Then to B that has an accumulated cost of 234 and so on. For this path to go from J to G the total cost is 248.

The algorithm starts as follows, first we have the path starting at J

```
Path = [('J', 0)]
```

then we have to check for all the other nodes what would be the cost to go

```
Path = [('J', 0), ('E', 37)]
Path = [('J', 0), ('B', 339)]
Path = [('J', 0), ('G', 946)]
Path = [('J', 0), ('H', 513)]
Path = [('J', 0), ('D', 984)]
Path = [('J', 0), ('F', 1482)]
Path = [('J', 0), ('C', 1193)]
Path = [('J', 0), ('A', 1775)]
Path = [('J', 0), ('I', 885)]
```

We see that from J we can go directly to F having a cost of 1482. Can we say this is the best way to go to F from J? Absolutely not!. We may have alternative paths going through other cities that have smaller cumulative cost. It is clear therefore that we have to expand the paths further but we have to do it smartly. We put all the expansions into a list (actually a heap) and expand the nodes from minimum cost to maximum cost. So the following iteration would be

```
Path = [('J', 0), ('E', 37), ('H', 224)]
Path = [('J', 0), ('H', 513)]
Path = [('J', 0), ('B', 339)]
Path = [('J', 0), ('E', 37), ('I', 769)]
Path = [('J', 0), ('E', 37), ('B', 626)]
Path = [('J', 0), ('F', 1482)]
Path = [('J', 0), ('G', 946)]
Path = [('J', 0), ('I', 885)]
Path = [('J', 0), ('E', 37), ('A', 2077)]
Path = [('J', 0), ('D', 984)]
Path = [('J', 0), ('E', 37), ('C', 1666)]
Path = [('J', 0), ('E', 37), ('D', 2755)]
Path = [('J', 0), ('E', 37), ('F', 1550)]
Path = [('J', 0), ('E', 37), ('G', 1479)]
Path = [('J', 0), ('C', 1193)]
Path = [('J', 0), ('A', 1775)]
```
This is, expanding the previous best path ```[('J', 0), ('E', 37)]``` whilst keeping all the others unexplored. Now, the best one is ```[('J', 0), ('E', 37), ('H', 224)]```, we will expand it and add to the list of paths. We do this process until we find the minimum path arriving to F.

## Using heap

To keep track of the paths a good data structure is the heap. When adding elements to a heap it costs O(log(N)) on average and O(1) to retrieve the minimum element. Heap is explained in this repository, I refer the reader there for further details.

## Complexity

Dijkstra is a good algorithm to find the minimum path but it has a huge drawback on computation time and memory. Recall that when we expand a city node we add (in general) N more nodes (where N is the number of cities). Time complexity is O(Elog(V)), where E is the number of edges and V the number of vertices (nodes). Log(V) comes from adding a node into the heap this is linear with the number of edges.  

## Practical implementation

I implemented the code in python witht he following definition for Node:

```python
class Node:
    def __init__(self, city: str):
        self.city = city

        self.cost = 0
        self.visited_cities = [city]
        self.path = [(city, 0)]

    # this is the comparison used by heapq to sort the node elements
    def __lt__(self, other):
        return self.cost < other.cost

    def add_step(self, city: str, cost: int):
        # add a cost to the node.
        if self.visited(city):
            raise ValueError(f"Node {city} has been visited previously")

        self.city = city
        self.cost = cost
        self.visited_cities.append(city)
        self.path.append((self.city, self.cost))

    def visited(self, city: str) -> bool:
        return True if city in self.visited_cities else False
```

Inside the object we define a path that is a list of a tuple (city name, cost). When we add a step what we do is to add a city to the path and update the cost to go to that city from the current city.

