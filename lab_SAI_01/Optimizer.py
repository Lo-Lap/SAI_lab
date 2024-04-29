from Evolution import Evolution
import random


class Optimizer:
    POPULATION_SIZE = 5000
    ITERATIONS = 10
    CHROMOSOME_LENGTH = 83
    SEED = 1488

    @staticmethod
    def optimize(field):
        rand = random.seed(Optimizer.SEED)
        evolution = Evolution(rand, field, Optimizer.CHROMOSOME_LENGTH, Optimizer.POPULATION_SIZE)

        population = [evolution.random_chromosome() for _ in range(Optimizer.POPULATION_SIZE)]

        for _ in range(Optimizer.ITERATIONS):
            mutated_population = [evolution.mutate(chromosome) for chromosome in population]
            selected_population = evolution.select(mutated_population)
            population = evolution.crossover(selected_population)

        # After final iteration, select the best chromosomes
        final_population = evolution.select(population)
        # The best chromosome is the first in the sorted list
        return final_population[0]

# The following line is just for example usage context, and would not be executed as a part of the module.
# if name == "main":
#     field = GameField()  # Assuming the GameField class is defined similarly
#     best_chromosome = Optimizer.optimize(field)
#     print("Best chromosome:", best_chromosome)