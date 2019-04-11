from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm()
some_values = ga.generate_initial_population()
print(some_values)
print(ga.get_fitness_vector())