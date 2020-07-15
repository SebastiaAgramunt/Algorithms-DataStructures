from random import random, randrange, seed
import sys
import string
from copy import deepcopy
import heapq

from typing import Dict, List

AdjacencyMatrixType = List[List[int]]


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


def get_city_names(N: int) -> (List[str], Dict[str, int], Dict[int, str]):
    chars = string.ascii_uppercase
    assert (
        len(chars) >= N
    ), f"There are more cities than characters. N must be {len(chars)} max"

    return (
        list(chars[:N]),
        {chars[i]: i for i in range(N)},
        {i: chars[i] for i in range(N)},
    )


def get_adjacency_matrix(cities: List[str], d_max: int) -> AdjacencyMatrixType:
    """
    Generate a random symmetric positive matrix representing the adjacency matrix. I.e. 
    a weighted undirected and fully connected graph.
    Input: 
        - cities: A list of cities names
        - d_max: maximum value of distance
    """
    N = len(cities)
    adjacency_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if random() > 0.8:
                val = randrange(d_max//3)
            else:
                val = randrange(d_max)
            adjacency_matrix[i][j] = val
            adjacency_matrix[j][i] = val

    return adjacency_matrix


def best_first_search(
    start: str,
    stop: str,
    cities: List[str],
    cities_str_int: Dict[str, int],
    adjacency_matrix: AdjacencyMatrixType,
):  
    """
    Return best first search
    """
    if start not in cities or stop not in cities:
        return None

    # we store the path node and the weight
    paths_heap = [Node(start)]

    step = -1
    while len(paths_heap) > 0:
        step+=1
        print(f"\nStep {step}:")
        for elem in paths_heap:
            print(f"\tPath = {elem.path}")
        
        node = heapq.heappop(paths_heap)
        print(f"\tpopping min path: {node.path}")

        current_city_str = node.city
        current_city_int = cities_str_int[current_city_str]

        if current_city_str == stop:
            return node.path

        min_weight, next_city_str = sys.maxsize, None
        for neighbor_city_str in cities:
            if not node.visited(neighbor_city_str):
                neighbor_city_int = cities_str_int[neighbor_city_str]
                weight = node.cost + adjacency_matrix[current_city_int][neighbor_city_int]

                new_node = deepcopy(node)
                new_node.add_step(neighbor_city_str, weight)
                heapq.heappush(paths_heap, new_node)


if __name__ == "__main__":

    seed(5)

    # number of cities
    N = 10
    # max dist value
    d_max = 5000

    # generating names and mappings between names (stirngs) and integer indexes
    cities, cities_str_int, cities_int_str = get_city_names(N)
    print(f"cities names:\n\t{cities}")
    print(f"mapping to numbers:\n\t{cities_str_int}")
    print(f"mapping to strings:\n\t{cities_int_str}")

    # we generate random distances between cities:
    adjacency_matrix = get_adjacency_matrix(cities, d_max)
    print(f"adjacency matrix: [")
    for row in adjacency_matrix:
        print(f"\t{row}")
    print("\t]")

    # pick random cities to look for
    starting_city = cities_int_str[randrange(N)]
    ending_city = cities_int_str[randrange(N)]

    print(f"starting city: {starting_city}")
    print(f"ending city: {ending_city}\n\n")

    path = best_first_search(
        start=starting_city,
        stop=ending_city,
        cities=cities,
        cities_str_int=cities_str_int,
        adjacency_matrix=adjacency_matrix,
    )

    print(f"\n\nBest path found:\n\t{path}")

