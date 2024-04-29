import numpy as np
import random


class Evolution:
    def __init__(self, rand, field, chromosome_length, population_size):
        self.random = rand
        self.field = field
        self.chromosome_length = chromosome_length
        self.population_size = population_size

    def mutate(self, chromosome):
        mutated = self.invert_bit(chromosome, random.randint(0, self.chromosome_length - 1))
        return mutated if self.field.testAnt(mutated) > self.field.testAnt(chromosome) else chromosome

    def invert_bit(self, chromosome, index):
        mutated = np.copy(chromosome)
        mutated[index] = not mutated[index]
        return mutated

    def select(self, population):
        scored_population = [(chromosome, self.field.testAnt(chromosome)) for chromosome in population]
        scored_population.sort(key=lambda x: x[1], reverse=True)
        return [chromosome for chromosome, score in scored_population[:len(population) // 2]]

    def crossover(self, parents):
        next_generation = []
        ind = 0
        if len(parents) % 2 == 1:
            next_generation.append(np.copy(parents[0]))
            ind += 1

        for i in range(ind, len(parents), 2):
            child1 = self.make_child(parents[i], parents[i + 1])
            child2 = self.make_child(parents[i + 1], parents[i])
            next_generation.extend([child1, child2, parents[i], parents[i + 1]])

        return next_generation[:self.population_size]

    def make_child(self, parent1, parent2):
        child = np.copy(parent1)
        quarter = self.chromosome_length // 4
        half = self.chromosome_length // 2

        child[:quarter] = parent2[:quarter]
        child[half:half + quarter] = parent2[half:half + quarter]

        return child

    def random_chromosome(self):
        return np.random.choice([True, False], size=self.chromosome_length)


# if name == "main":
#     # Example usage
#     field = GameField()
#     evolution = Evolution(field, chromosome_length=100, population_size=50)
#     initial_population = [evolution.random_chromosome() for _ in range(50)]
#     selected = evolution.select(initial_population)
#     offspring = evolution.crossover(selected)
