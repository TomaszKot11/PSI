from Algorithm import Algorithm
import time
import math

class AAsteriskAlgorithm(Algorithm):


  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()
    paths = []
    weights = []
    for i in range(self.city_storage.number_cities):
      next_path = self.perform_a_star_algorithm(i)
      # append current node
      next_path.append(i)
      paths.append(next_path)
      weights.append(self.city_storage.get_total_weight_for_path(next_path))

    # get min value from specific pathsss
    min_val = min(weights)
    min_val_index = weights.index(min_val)

    end_time = time.time()

    return { 'time': (end_time - start_time), 'cities': paths[min_val_index], 'path_cost': min_val }

  def perform_a_star_algorithm(self, starting_node):
    all_cities = self.city_storage.cities
    visited = [ starting_node ]
    all_cities_copy = all_cities.copy()
    del all_cities_copy[starting_node]
    not_visited = all_cities_copy
    while(len(visited) < self.city_storage.number_cities):
      # each vertex have path to each so
      current_vertex = visited[-1]
      local_dictionary = {}
      for i in not_visited:
        # from current_node to the final ndoe - here we assume that the current node
        # is the final node and we use heuristic to compute the value
        h = self.heuristic(i[0], current_vertex)
        # from start_node to current_node
        visited_copy = visited.copy()
        visited_copy.append(i[0])
        g = self.city_storage.get_total_weight_for_path(visited_copy)
        f = h + g
        local_dictionary[i[0]] = f
      sorted_words = sorted(local_dictionary.items(), key=lambda x: int(x[1]))
      # we get the last tuple
      next_vertex = sorted_words[0][0]
      not_visited.remove(all_cities[next_vertex])
      visited.append(next_vertex)

    return visited




  def heuristic(self, start_node, goal_node):
    # is our heuristic
    all_cities = self.city_storage.cities
    # x
    dx = abs(all_cities[start_node][1] - all_cities[goal_node][1])
    # y
    dy = abs(all_cities[start_node][2] - all_cities[goal_node][2])
    return max(dx, dy)