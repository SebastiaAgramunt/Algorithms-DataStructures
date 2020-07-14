# Directed graphs
A ***directed graph*** is a graph in which the direction of the edges is defined. As mentioned in the above example there is an edge ```("A", "B")``` and not ```("B", "A")``` defining a directionality. We can go from A to B but not viceversa.

A ***directed acyclic graph*** is a directed graph that contains no loops. This is, given any vertex ```V``` there is no path starting and ending at ```V```.

A ***tree*** is a directed acyclic graph whose nodes have just one parent, i.e. each node can have just two sons (0, 1 or 2 sons).
