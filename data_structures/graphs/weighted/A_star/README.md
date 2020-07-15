# A* search

It is an algorithm to find a good short path (not the minimum) in between two nodes in the graph. The graph has to be weighted and **positive definite** (all weights have to be positive). Also, we need some sort of heuristic to approximate a good direction, this is what we call an **informed search**.

A typlical example of such algorithm is to draw a path in between two cities A and B such that the path is small according to the heuristic of minimum distance. 

To guide intuition imagine we depart from city A and this city is connected to C, D and E. Which city will we visit next? Depends on the heuristic, we calculate the approximated distance between C, D and E to B and choose to expand the one that minimises the distance (the most promissing). We keep the other nodes ordered list (in the sense of most promissing one) because maybe we can expand later on. Normally this list is implemented as a heap data structure as it is O(1) to pop the minimum element and O(NlogN) to add a new node.

We are going to see how this works on an example 