from CityStorage import CityStorage
# from BruteForce import BruteForce
from PlotDrawer import PlotDrawer
from NNAlgorithm import NNAlgorithm
from BfsBruteForce import BfsBruteForce
from DfsBruteForce import DfsBruteForce
from OrdinaryBruteForce import OrdinaryBruteForce

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

def print_result(result):
  for key, value in result.items():
    print(str(key) + ' ' + str(value))

first_city_storage = CityStorage.with_given_cities(first_test_array)


bfs_algorithm = BfsBruteForce(first_city_storage)
bfs_result = bfs_algorithm.perform()
print('BFS algorithm')
print_result(bfs_result)

print('DFS algorithm')
dfs_algorithm = DfsBruteForce(first_city_storage)
dfs_result = dfs_algorithm.perform()

print_result(dfs_result)

print('Ordinary brute force:')
ordinary_brute_force_algorithm = OrdinaryBruteForce(first_city_storage)
ordinary_brute_result = ordinary_brute_force_algorithm.perform()
print_result(ordinary_brute_result)

print('NN algorithm:')
nn_algorithm = NNAlgorithm(first_city_storage)
nn_algorithm_result = nn_algorithm.perform()
print_result(nn_algorithm_result)

# print('---------')
# print('---------')
# print('---------')
# print('time: ' + str(nn_algorithm_result['time']))
# print('reuslt: ' + str(nn_algorithm_result['cities']))
# print('---------')
# print('---------')
# print('---------')

# PlotDrawer(cities = result['cities'], title = 'Brute force algorithm')
# PlotDrawer(cities = nn_algorithm_result['cities'], title = 'Brute force algorithm')



# PlotDrawer(times = [ result['time'] ])