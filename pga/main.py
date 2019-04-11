from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(population_size =  10)
for i in range(10):
    print('GA with one iteration: ')
ga.perform()
for i in range(10):
    print('GA with 5 iteration: ')
ga.perform(5)
