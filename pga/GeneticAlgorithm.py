import numpy as np
from itertools import compress

class GeneticAlgorithm:

  def __init__(self, population_size = 8, mutation_rate = 0.25, chromosome_length = 7):
    self.population_size = population_size
    self.mutation_rate = mutation_rate
    self.chromosome_length = chromosome_length

  def perform(self, iterations = 1):
    self.generate_initial_population()
    self.update_fitness_vector()

    for i in range(iterations):
      # generate parents
      parent_pairs = self.select_parents()
      # generate children
      children = np.array([ self.generate_children(parent_pair) for parent_pair in parent_pairs ])

      mutated_children = [self.mutate(child, self.mutation_rate) for child in children]
      self.population = np.array(mutated_children)
      self.update_fitness_vector
      self.print_new_population_info(i)

  # selects parents for the next generation
  def select_parents(self):
    relative_fitness = np.array(self.population_fitness_vector) / np.sum(self.population_fitness_vector)
    parents = []
    # generates parents pairs
    for i in range(self.population_size):
      parents.append([self.weighted_random_choice(), self.weighted_random_choice()])

    return np.array(parents)


  # (helper function for select_parents) roulette wheel of selection parents
  def weighted_random_choice(self):
    max = np.sum(self.population_fitness_vector)
    pick = np.random.uniform(0, max)
    current = 0
    for idx, chromosome in enumerate(self.population):
        current += self.population_fitness_vector[idx]
        if current > pick:
            return chromosome

  # generates the children genome using randomly
  # generate locus from two parents
  def generate_children(self, parent_pair):
    parent_first = parent_pair[0]
    parent_second = parent_pair[1]
    # single point crossover
    # but random locus
    locus_index = np.random.randint(0, self.chromosome_length)
    parent_second_last_index = len(parent_second)

    return np.array(parent_first[0:locus_index].tolist() +  parent_second[locus_index:parent_second_last_index].tolist())

  # prints the current population info
  def print_new_population_info(self, population_no):
    print('----------')
    print('The population number: ' + str(population_no + 1))
    print('----------')
    print('The greatest value: ' + str(self.get_the_best_genome_value()) + ' for chromosome: ' + str(self.get_best_genome()))
    print('----------')

  # mutates the genes randomly in the child
  def mutate(self, chromosome, mutation_rate):
    chromosome = np.array(chromosome)
    random_value = np.random.rand(self.chromosome_length)
    # see which genes to mutate
    boolean_mutation_values = random_value < self.mutation_rate
    chromosome[boolean_mutation_values] = [ self.bit_invert(value) for value in chromosome[boolean_mutation_values]]

    return chromosome

    # helper function for inverting bits
  def bit_invert(self, value):
    if value == '1':
      return '0'
    else:
      return '1'

  # generates the random initial population
  def generate_initial_population(self, chromosome_length = 7):
    self.population = []
    for i in range(0, self.population_size):
      random_values = np.random.randint(2, size = chromosome_length)
      self.population.append(random_values)

    self.population = np.array(self.population)

    return self.population

  # updates the fitness_vector for current population
  def update_fitness_vector(self):
    self.population_fitness_vector = []
    for i in self.population:
      value = ''
      for j in i:
        value += str(j)
      self.population_fitness_vector.append(self.calculate_fitness_function(int(value, 2)))

  # calculates the fitness function
  def calculate_fitness_function(self, value):
    return 2*(value**2 + 1)

  # get the best genome foor current population
  def get_best_genome(self):
    best_genome_index = self.population_fitness_vector.index(max(self.population_fitness_vector))

    return self.population[best_genome_index]

  # gets the best value for current population
  def get_the_best_genome_value(self):
    return max(self.population_fitness_vector)
