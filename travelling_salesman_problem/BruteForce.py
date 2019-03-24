from Algorithm import Algorithm
from CityStorage import CityStorage
import numpy as np
import itertools

# pip install numpy
# iterates throug all
# permutations and gets the minium weigth road
class BruteForce(Algorithm):
  def __init__(self, city_storage):
    self.city_storage = city_storage

  def perform(self):
    cities_as_list = self.city_storage.cities_as_list()
    all_permutations = list(itertools.permutations(cities_as_list))

    # append the first city to each tuple as this is the city to which we will return
    for idx, val in enumerate(all_permutations):
      historic_tuple = val
      new_tuple = (*val, val[0])
      all_permutations[idx] = new_tuple


    total_distances = []
    distances = []

    for i in all_permutations:
      # here we have a tuple
      count = len(i)
      local_distances = []

      for j in range(0, count - 1):
        city_first = i[j]
        city_second = i[j+1]

        local_distances.append(self.city_storage.calculate_distance_using_indexes(city_first[0], city_second[0]))
      total_distances.append(sum(local_distances))
      distances.append(local_distances)

    # get the minimum distance
    distances_list = np.array(total_distances).tolist()
    min_val = min(distances_list)
    min_val_index = distances_list.index(min_val)

    return { 'weight': min_val, 'cities': list(all_permutations)[min_val_index] }
