import random

class GeneticAlgorithm:

  def __init__(self, population_size = 8, mutation_rate = 0.001, number_iterations = 1000):
    self.population_size = population_size
    self.number_iterations = number_iterations
    self.mutation_rate = number_iterations

  # generates binary initial population
  def generate_initial_population(self, genes):
    for _ in range(self.population_size):
      genes.append('{0:07b}'.format(random.randint(1, 127)))

  # calculates fitness function
  # in our case we are optimizing 2*(x^2 + 1) function
  def calculate_fitness_function(self, x):
    value = int(x, 2)

    return 2*(value**2 + 1)

  # calculates the sum of all fitness functions
  def roulette_fitness_sum(self, genes):
    return sum(self.calculate_fitness_function(x) for x in genes)

  def roulette_probability_for_gene(self, x, sum):
    return self.calculate_fitness_function(x) / sum

  # selects arents to the next generation
  # based on roulette roulette wheel algorithm
  def select_parents(self, genes):
    sum = self.roulette_fitness_sum(genes)
    roulette = [self.roulette_probability_for_gene(genes[0], sum)]
    for i in range(1, len(genes)):
      roulette.append(self.roulette_probability_for_gene(genes[i], sum))
      roulette[i] += roulette[i-1]
    return [genes[self.get_chosen_gene_index(roulette)] for _ in range(len(genes))]

  # helper function which gets the index of
  # gene which was chosen to the next population
  def get_chosen_gene_index(self, roulette):
    val = random.random()
    index = 0
    return next((i for i in range(len(roulette)) if val < float(roulette[i])),
                index)

  # makes crossover between genes
  # choosing the random locus
  def crosover_genes(self, genes):
    random.shuffle(genes)
    crossed_genes=[]
    for i in range(0,len(genes),2):
      locus=random.randint(0,len(genes[0]))
      crossed_genes.extend((
          self.combine_genes(genes[i + 1], genes[i], locus),
          self.combine_genes(genes[i], genes[i + 1], locus),
      ))
    return crossed_genes

  # helper function for glueing two genes together
  def combine_genes(self, parent_first, parent_second, locus):
    return parent_first[:locus] + parent_second[locus:]

  # performs mutation in the whole generation
  def mutate_genes(self, genes):
    return [self.mutate_gen(x) for x in genes]

  # performs mutation of a gene
  # accordingly to mutation rate
  def mutate_gen(self, gen):
    if random.random() < self.mutation_rate:
      locus = random.randint(0, len(gen) - 1)
      temp = list(gen)
      temp[locus] = '0' if temp[locus] == '1' else '1'
      return ''.join(temp)
    return gen

  # prints population inormaiton
  def print_population_information(self, genes):
    print(f'For genes: {str(genes)}')
    print(f'Max value is: {str(self.get_max_value_for_population(genes))}')

  #  gets the mex fitness value of the fitness function
  # from the whole population
  def get_max_value_for_population(self, genes):
    temp_array = [self.calculate_fitness_function(x) for x in genes]
    return max(temp_array)

  # performs the whole agenetic algorithm
  def perform(self):
    all_genes = list(range(1,128))
    genes = [
        "{:07b}".format(all_genes.pop(random.randint(0, len(all_genes))))
        for _ in range(self.population_size)
    ]
    for _ in range(self.number_iterations):
      genes = self.select_parents(genes)
      genes = self.crosover_genes(genes)
      genes = self.mutate_genes(genes)
      self.print_population_information(genes)
