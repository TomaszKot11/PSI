from Algorithm import Algorithm
from CityStorage import CityStorage
import numpy as np
import itertools
import time

# pip install numpy
# iterates throug all
# permutations and gets the minium weigth road
class OrdinaryBruteForce(Algorithm):
  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    start_time = time.time()

    cities_as_list = self.city_storage.cities_as_list()
    all_permutations = list(itertools.permutations(cities_as_list))
    all_permutations_indexes = []
    for i in all_permutations:
      new_arr = list(map(lambda x: x[0], i))
      new_arr.append(new_arr[0])
      all_permutations_indexes.append(new_arr)
    result = min(all_permutations_indexes, key = lambda c: self.city_storage.get_total_weight_for_path(c) )

    min_val = self.city_storage.get_total_weight_for_path(result)

    # My custom - very weak implementation
    # append the first city to each tuple as this is the city to which we will return
    # for idx, val in enumerate(all_permutations):
    #   historic_tuple = val
    #   new_tuple = (*val, val[0])
    #   all_permutations[idx] = new_tuple


    # total_distances = []
    # distances = []

    # for i in all_permutations:
    #   # here we have a tuple
    #   count = len(i)
    #   local_distances = []

    #   for j in range(0, count - 1):
    #     city_first = i[j]
    #     city_second = i[j+1]

    #     local_distances.append(self.city_storage.calculate_distance_using_indexes(city_first[0], city_second[0]))
    #   total_distances.append(sum(local_distances))
    #   distances.append(local_distances)

    # # get the minimum distance
    # distances_list = np.array(total_distances).tolist()
    # min_val = min(distances_list)
    # min_val_index = distances_list.index(min_val)

    end_time = time.time()

    return { 'time': (end_time - start_time), 'cities': result, 'path_cost': min_val }
