from CityStorage import CityStorage
from BruteForce import BruteForce
from PlotDrawer import PlotDrawer
from NNAlgorithm import NNAlgorithm

# city_storage = CityStorage(7)

# brute_force = BruteForce(city_storage)

# brute_force.perform()

# print('with fixed cities:')



first_test_array = [
  [0, 23, 23],
  [1, 45, 32],
  [2, 34, 43],
  [3, 56, 65],
  [4, 12, 99],
  [5, 56, 56],
  [6, 43, 21]
]

second_test_array = [
  [0, 23, 89],
  [1, 12, 32],
  [2, 45, 56],
  [3, 93, 68],
  [4, 45, 67],
  [5, 56, 43],
  [6, 32, 12]
]

# Brute force algorithm
first_city_storage = CityStorage.with_given_cities(first_test_array)

brute_force = BruteForce(first_city_storage)

result = brute_force.perform()

print('---------')
print('---------')
print('---------')
for key, value in result.items():
  print(str(key) + ' ' + str(value))
print('---------')
print('---------')
print('---------')



# PlotDrawer(times = [ result['time'] ])

nn_algorithm = NNAlgorithm(first_city_storage)
nn_algorithm_result = nn_algorithm.perform()

print('---------')
print('---------')
print('---------')
print('time: ' + str(nn_algorithm_result['time']))
print('reuslt: ' + str(nn_algorithm_result['cities']))
print('---------')
print('---------')
print('---------')

PlotDrawer(cities = result['cities'], title = 'Brute force algorithm')
PlotDrawer(cities = nn_algorithm_result['cities'], title = 'Brute force algorithm')
