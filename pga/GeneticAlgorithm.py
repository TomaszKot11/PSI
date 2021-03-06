import random

class GeneticAlgorithm:

  def __init__(self, population_size = 8, mutation_rate = 0.001, number_iterations = 1000):
    self.population_size = population_size
    self.number_iterations = number_iterations
    self.mutation_rate = number_iterations

  # generates binary initial population
  def generate_initial_population(self, genes):
    for i in range(self.population_size):
      genes.append('{0:07b}'.format(random.randint(1, 127)))

  # calculates fitness function
  # in our case we are optimizing 2*(x^2 + 1) function
  def calculate_fitness_function(self, x):
    value = int(x, 2)

    return 2*(value**2 + 1)

  # calculates the sum of all fitness functions
  def roulette_fitness_sum(self, genes):
    sum = 0
    for x in genes:
      sum += self.calculate_fitness_function(x)

    return sum

  def roulette_probability_for_gene(self, x, sum):
    return self.calculate_fitness_function(x) / sum

  # selects arents to the next generation
  # based on roulette roulette wheel algorithm
  def select_parents(self, genes):
    roulette = []
    sum = self.roulette_fitness_sum(genes)
    roulette.append(self.roulette_probability_for_gene(genes[0], sum))
    for i in range(1, len(genes)):
      roulette.append(self.roulette_probability_for_gene(genes[i], sum))
      roulette[i] += roulette[i-1]
    parent_genes = []
    for i in range(0, len(genes)):
      parent_genes.append(genes[self.get_chosen_gene_index(roulette)])

    return parent_genes

  # helper function which gets the index of
  # gene which was chosen to the next population
  def get_chosen_gene_index(self, roulette):
    val = random.random()
    index = 0
    for i in range(0, len(roulette)):
      if val < float(roulette[i]):
        return i
    return index

  # makes crossover between genes
  # choosing the random locus
  def crosover_genes(self, genes):
    random.shuffle(genes)
    crossed_genes=[]
    for i in range(0,len(genes),2):
      locus=random.randint(0,len(genes[0]))
      crossed_genes.append(self.combine_genes(genes[i+1],genes[i],locus))
      crossed_genes.append(self.combine_genes(genes[i],genes[i+1],locus))

    return crossed_genes

  # helper function for glueing two genes together
  def combine_genes(self, parent_first, parent_second, locus):
    crossed_gene = parent_first[:locus] + parent_second[locus:]

    return crossed_gene

  # performs mutation in the whole generation
  def mutate_genes(self, genes):
    mutated_genes = []
    for x in genes:
      mutated_genes.append(self.mutate_gen(x))

    return mutated_genes

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
    print('For genes: ' + str(genes))
    print('Max value is: ' + str(self.get_max_value_for_population(genes)))

  #  gets the mex fitness value of the fitness function
  # from the whole population
  def get_max_value_for_population(self, genes):
    temp_array = []
    for x in genes:
      temp_array.append(self.calculate_fitness_function(x))

    return max(temp_array)

  # performs the whole agenetic algorithm
  def perform(self):
    all_genes=[]
    for i in range(1,128):
      all_genes.append(i)
    genes=[]
    for i in range(0, self.population_size):
      genes.append("{:07b}".format(all_genes.pop(random.randint(0, len(all_genes)))))


    for i in range(self.number_iterations):
      genes = self.select_parents(genes)
      genes = self.crosover_genes(genes)
      genes = self.mutate_genes(genes)
      self.print_population_information(genes)
