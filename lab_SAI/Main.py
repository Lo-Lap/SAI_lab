from GameField import GameField
from Optimizer import Optimizer

FIELD_FILENAME = "field.csv"


def main():
    field = GameField()
    field.fill(FIELD_FILENAME)
    best_chromosome = Optimizer.optimize(field)
    result = field.testAnt(best_chromosome)
    print(f"Your result is {result}")
    print("Max is 89")


if __name__ == "main":
    main()
