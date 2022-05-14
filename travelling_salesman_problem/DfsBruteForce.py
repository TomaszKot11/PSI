from Algorithm import Algorithm
from CityStorage import CityStorage
import numpy as np
import itertools
import time

# pip install numpy
# iterates throug all
# permutations and gets the minium weigth road
class DfsBruteForce(Algorithm):
  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()
    paths = []
    weights = []
    for i in range(self.city_storage.number_cities):
      # generate paths
      new_path = self.dfs(i)
      new_path.append(new_path[0])
      paths.append(new_path)
      weights.append(self.city_storage.get_total_weight_for_path(new_path))

    min_val = min(weights)
    min_val_index = weights.index(min_val)

    end_time = time.time()

    return { 'time': (end_time - start_time), 'cities': paths[min_val_index], 'path_cost': min_val }

  # dfs for completee graph
  def dfs(self, starting_node):
    # prepare the graph
    graph = {
        i: self.generate_sorted_range(i, self.city_storage.number_cities)
        for i in range(self.city_storage.number_cities)
    }
    return self.core_dfs(graph, starting_node)

  def core_dfs(self, graph, start):
    visited, stack = set(), [start]
    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.add(vertex)
        stack.extend(graph[vertex] - visited)
    return list(visited)


  def generate_sorted_range(self, current_node, total_number):
    temp = [i for i in range(total_number) if i != current_node]
    # return set(temp.sort())
    return set(temp)

