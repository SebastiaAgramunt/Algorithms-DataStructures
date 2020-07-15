# Best first search

Best first search is applied to a weighted graph to find a "good" path between two nodes. By good we mean that it can be the minimum path but in general is not, and it is smaller than a random path. We achieve this close to minimum path using a very simple heuristic.


## How best first search work?

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
Cost to go to A: 1775
Cost to go to B: 339
Cost to go to C: 1193
Cost to go to D: 984
Cost to go to E: 37
Cost to go to F: 1482
Cost to go to G: 946
Cost to go to H: 513
Cost to go to I: 885
```

Now we decide to get rid of all the potential paths generated and choose to expand the most promissing path (this is the key difference between BFS and Dijkstra), i.e. we jsut expand the path ```[('J', 0), ('E', 37)]```. Now for the next step we have

```
Cost to go to A: 2077
Cost to go to B: 626
Cost to go to C: 1666
Cost to go to D: 2755
Cost to go to F: 1550
Cost to go to G: 1479
Cost to go to H: 224
Cost to go to I: 769
```
Notice that the option to go to E has disapeared because it's already in our current path. We find the minimum to be the path going to H so we pick ```[('J', 0), ('E', 37), ('H', 224)]```  for the next path to expand. We do this process until we hit the minimum path finishing at F (our ending point).

In best first search we get the following path as a good approach for minimum

```
BFS_min = ('J', 0), ('E', 37), ('H', 224), ('B', 234), ('G', 248), ('C', 1860), ('D', 2452), ('I', 5363), ('F', 6290)]
```
However if we run Dijkstra on the same data we get

```
Min_path = [('J', 0), ('F', 1482)]
```

which clearly has less cost than BFS and is actually the minimum path (check explanation for Dijkstra).

## Complexity

It is very fast as we expand just one node at a time. For N nodes the time would be O(N). Also it is O(1) in space because we just need to store one node at each step.