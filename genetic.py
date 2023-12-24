import random
class Genetic:
    bestOfGenerationsFitness = []
    Avg = []
    maxFitness = 0
    
    def getBOG(self):
        return self.bestOfGenerationsFitness

    def calcAvg(self , array):
        sum = 0
        for gen in array:
            sum += self.__fitness(gen)
        self.Avg.append(sum/len(array))

    def getAvg(self):
        return self.Avg
    
    def clearBOG(self):
        self.bestOfGenerationsFitness.clear()
    
    def clearAvg(self):
        self.Avg.clear()
    def __init__(self , n , populationCount , csrate , mrrate , elitrate , generations):
        self.n = n
        self.maxFitness = ((n+1) * n / 2) - n
        self.populationCount = populationCount
        self.csrate = csrate
        self.mrrate = mrrate
        self.elitrate = elitrate
        self.generations = generations

    def __generate_individual(self):
        return random.sample(range(self.n), self.n)

    def __fitness(self , individual):
        clashes = 0
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                if abs(i - j) == abs(individual[i] - individual[j]):
                    clashes += 1
        return self.maxFitness - clashes

    def __crossover(self , parent1, parent2):
        if (random.random() < self.csrate):
            crossover_point = random.randint(1, self.n-2)
            child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
            child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
            return [child1 , child2]
        else:
            return [parent1 , parent2]

    def __mutate(self , individual):
        mutation_point1, mutation_point2 = random.sample(range(self.n), 2)
        individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]

    def solution(self):
        population = []
        generation = 0
        population = [self.__generate_individual() for _ in range(self.populationCount)]

        for generation in range(self.generations):

            population = sorted(population, key=lambda x: self.__fitness(x), reverse=True)

            self.bestOfGenerationsFitness.append(self.__fitness(population[0]))
 
            #Calc Avg
            self.calcAvg(population)
            if self.__fitness(population[0]) == self.maxFitness:
                return(f"Solution found in generation {generation + 1}: {population[0]}")
            
            #Elitism
            new_population = []
            elitcount = abs(int(self.populationCount * self.elitrate))
            for i in range(elitcount):
                new_population.append(population[i])

            # new_population = [population[:elitcount]]  # Elitism: Keep the best individual
            while len(new_population) < self.populationCount:
                parent1, parent2 = random.choices(population[:5], k=2)  # Tournament selection
                [child1 , child2] = self.__crossover(parent1, parent2)
                if random.random() < self.mrrate:  # 10% chance of mutation
                    self.__mutate(child1)
                if random.random() < self.mrrate:
                    self.__mutate(child2)
                new_population.append(child1)
                new_population.append(child2)

            population = new_population
        return (f"Best Effort: {population[0]} , fitness:{self.__fitness(population[0])}/{self.maxFitness}")
