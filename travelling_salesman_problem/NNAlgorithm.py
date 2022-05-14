from Algorithm import Algorithm
import time

# nearest neighbour algorithm(greedy algorithm)
class NNAlgorithm(Algorithm):

  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()
    all_visited = []
    for i in range(self.city_storage.number_cities):
      new_arr = list(map(lambda x: x[0], self.perform_nn_with_starting(i)))
      all_visited.append(new_arr)

    result = min(all_visited, key = lambda c: self.city_storage.get_total_weight_for_path(c) )
    min_val = self.city_storage.get_total_weight_for_path(result)
    end_time = time.time()

    return { 'time': (end_time - start_time), 'cities': result, 'path_cost': min_val }

  def perform_nn_with_starting(self, starting_node):
    unvisited = self.city_storage.cities.copy()
    temp = unvisited[starting_node]
    del unvisited[starting_node]
    visited = [temp]
    while unvisited:
      unvisited.sort(key = lambda c: self.city_storage.calculate_distance_using_indexes(visited[-1][0], c[0]))
      next_city = unvisited[0]
      visited.append(next_city)
      unvisited.remove(next_city)
    # append the first element of the visited to close the cycle
    visited.append(visited[0])

    return visited

