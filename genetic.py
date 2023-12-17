import random
class Genetic:
    bestOfGenerationsFitness = []
    def __init__(self , populationCount , csrate , mrrate , elitrate , generations):
        self.populationCount = populationCount
        self.csrate = csrate
        self.mrrate = mrrate
        self.elitrate = elitrate
        self.generations = generations

    def __generate_individual(self):
        return random.sample(range(8), 8)

    def __fitness(self , individual):
        clashes = 0
        for i in range(7):
            for j in range(i + 1, 8):
                if abs(i - j) == abs(individual[i] - individual[j]):
                    clashes += 1
        return 28 - clashes  # 28 is the maximum fitness (no clashes)

    def __crossover(self , parent1, parent2):
        if (random.random() < self.csrate):
            crossover_point = random.randint(1, 6)
            child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
            return child
        else:
            return parent1

    def __mutate(self , individual):
        mutation_point1, mutation_point2 = random.sample(range(8), 2)
        individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]

    def solution(self):
        population = []
        generation = 0
        population = [self.__generate_individual() for _ in range(self.populationCount)]

        for generation in range(self.generations):

            population = sorted(population, key=lambda x: self.__fitness(x), reverse=True)

            self.bestOfGenerationsFitness.append(self.__fitness(population[0]))

            if self.__fitness(population[0]) == 28:
                return(f"Solution found in generation {generation + 1}: {population[0]}")
            
            #Elitism
            new_population = []
            elitcount = abs(int(self.populationCount * self.elitrate))
            for i in range(elitcount):
                new_population.append(population[i])

            # new_population = [population[:elitcount]]  # Elitism: Keep the best individual
            while len(new_population) < self.populationCount:
                parent1, parent2 = random.choices(population[:5], k=2)  # Tournament selection
                child = self.__crossover(parent1, parent2)
                if random.random() < self.mrrate:  # 10% chance of mutation
                    self.__mutate(child)
                new_population.append(child)

            population = new_population
        return (f"Best Effort: {population[0]} , fitness:{self.__fitness(population[0])}/28")
