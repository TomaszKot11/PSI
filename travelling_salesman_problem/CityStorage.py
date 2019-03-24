from random import randint
import numpy as np
import math

# TODO: make sure cities have unique coordinates ?
class CityStorage:
  def __init__(self, number_cities, with_given_arr = False, given_cities = []):
    self.number_cities = number_cities
    if not(with_given_arr):
      self.generate_cities()
    else:
      self.cities = given_cities

  @classmethod
  def with_given_cities(cls, cities):
    citiesCount = len(cities)
    cities = cities
    return cls(citiesCount, True, cities)

  def generate_cities(self):
    self.cities = []
    for i in range(0, self.number_cities):
      self.cities.append([ i, self.get_random_in_range(), self.get_random_in_range() ])

  def get_random_in_range(self):
    return randint(0, 100)

  def calculate_distance_using_indexes(self, city_one_i, city_two_i):
    city_one_c = self.get_city_coordinates(city_one_i)
    city_two_c = self.get_city_coordinates(city_two_i)
    x_diff = city_one_c[0] - city_two_c[0]
    y_diff = city_one_c[1] - city_two_c[1]
    return math.sqrt((x_diff ** 2) + (y_diff ** 2))

  def calculate_total_distance_for_given_cities(self, given_cities):
    # for i in given_cities:
    raise NotImplementedError('Not implemented method called')

  def get_city_coordinates(self, city_index):
    return (self.cities[city_index][1], self.cities[city_index][2])

  def cities_as_list(self):
    return np.array(self.cities).tolist()
