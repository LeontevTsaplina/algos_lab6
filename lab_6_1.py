import random
import networkx as nx
import time
import matplotlib.pyplot as plt
from statistics import mean


def random_graph(vertices_count: int, edges_count: int) -> nx.Graph:
    """
    Function that generate random weighted graph with input count of vertices and edges

    :param vertices_count: vertices count
    :param edges_count: edges count
    :type vertices_count: int
    :type edges_count: int
    :return: generated weighted graph
    :rtype: nx.Graph
    """

    if edges_count > vertices_count ** 2 / 2:
        raise ValueError("Edges count must be less then vertices count ^ 2 / 2")

    if edges_count < vertices_count:
        raise ValueError("Vertices count must be bigger then edges count")

    result = nx.Graph()

    for i in range(vertices_count):
        result.add_node(i)

    possible_vertices_in_matrix = [elem for elem in range(vertices_count ** 2) if elem // vertices_count < elem % vertices_count]

    for row in range(vertices_count - 1):
        column = random.randint(row + 1, vertices_count - 1)

        result.add_edge(row, column)

        possible_vertices_in_matrix.remove(row * vertices_count + column)

    edges_left = edges_count - vertices_count

    random_vertices = random.sample(possible_vertices_in_matrix, edges_left)

    for elem in random_vertices:
        result.add_edge(elem // vertices_count, elem % vertices_count, weight=random.randint(1, 100))

    return result


# Generating graph
my_graph = random_graph(100, 500)

# Print paths
print(nx.single_source_dijkstra(my_graph, 7)[1])
print(nx.single_source_bellman_ford(my_graph, 7)[1])

dijkstra_times = []
bellman_ford_times = []

# Counting time of working
for _ in range(10):
    start_time = time.perf_counter()
    nx.single_source_dijkstra(my_graph, 7)
    end_time = time.perf_counter()
    dijkstra_times.append(end_time - start_time)

# Counting time of working
for _ in range(10):
    start_time = time.perf_counter()
    nx.single_source_bellman_ford(my_graph, 7)[1]
    end_time = time.perf_counter()
    bellman_ford_times.append(end_time - start_time)

# Print results
print()
print("Dijkstra's mean time:", mean(dijkstra_times))
print("Bellman-Ford's mean time", mean(bellman_ford_times))

plt.bar([1, 2], [mean(dijkstra_times), mean(bellman_ford_times)], width=0.2)
plt.ylabel('time')
plt.show()
