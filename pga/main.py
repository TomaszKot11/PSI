from GeneticAlgorithm import GeneticAlgorithm

ga = GeneticAlgorithm(population_size =  5, chromosome_length = 7)
for i in range(10):
    print('GA with one iteration: ')
ga.perform()
for i in range(10):
    print('GA with 20 iteration: ')
ga.perform(20)
