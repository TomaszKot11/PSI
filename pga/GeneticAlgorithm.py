import numpy as np

class GeneticAlgorithm:

  def __init__(self, population_size = 8):
    self.population_size = 8

  #TODO: make use of doubles?
  def generate_initial_population(self, chromosome_length = 7):
    self.population = []
    for i in range(0, self.population_size):
      random_values = np.random.randint(2, size = chromosome_length)
      array = []
      for i in random_values:
        array.append(i)
      self.population.append(array)

    return self.population

  def get_fitness_vector(self):
    self.population_vector = []
    for i in self.population:
      value = ''
      for j in i:
        value += str(j)
      self.population_vector.append(self.calculate_fitness_function(int(value, 2)))

  def calculate_fitness_function(self, value):
    return 2*(value**2 + 1)

  def perform(self):
    self.generate_initial_population()
    self.get_fitness_vector()
