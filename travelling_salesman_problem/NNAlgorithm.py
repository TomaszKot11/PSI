from Algorithm import Algorithm
import time

# nearest neighbour algorithm(greedy algorithm)
class NNAlgorithm(Algorithm):

  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()

    unvisited = self.city_storage.cities.copy()
    visited = [unvisited.pop()]
    while unvisited:
      next_city = min(unvisited, key=lambda c: self.city_storage.calculate_distance_using_indexes(visited[-1][0], c[0]))
      visited.append(next_city)
      unvisited.remove(next_city)
    # append the first element of the visited to close the cycle
    visited.append(visited[0])
    end_time = time.time()

    return { 'time': (end_time - start_time), 'cities': visited }

