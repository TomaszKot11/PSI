from Algorithm import Algorithm
from CityStorage import CityStorage
import numpy as np
import itertools
import time

# 'visit all neighbours before goind deeper'
# we assume all nodes have connection to all nodes
class BfsBruteForce(Algorithm):
  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()
    paths = []
    weights = []
    for i in range(self.city_storage.number_cities):
      # generate paths
      new_path = self.bfs(i)
      paths.append(new_path)
      weights.append(self.city_storage.get_total_weight_for_path(new_path))

    min_val = min(weights)
    min_val_index = weights.index(min_val)

    end_time = time.time()


    return { 'time': (end_time - start_time), 'cities': paths[min_val_index], 'path_cost': min_val }

  def bfs(self, starting_node):
    visited = [ starting_node ]
    while (len(visited) < self.city_storage.number_cities):
      for i in range(self.city_storage.number_cities):
        # skip the starting node
        if i == starting_node:
          continue
        if i not in visited:
          visited.append(i)

    visited.append(starting_node)

    return visited
