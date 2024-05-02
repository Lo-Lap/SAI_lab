from GameField import GameField
from task import Optimizer
import json

FIELD_FILENAME = "field.csv"


def main():
    field = GameField()
    field.fill(FIELD_FILENAME)
    best_chromosome = Optimizer.optimize(field)
    result = field.testAnt(best_chromosome)
    print(f"Your result is {result}")
    print("Max is 89")
    grade = 0

    if result >= 50:
        grade = 1
    elif result >= 60:
        grade = 2
    elif result >= 80:
        grade = 3
    elif result >= 82:
        grade = 4
    elif result >= 84:
        grade = 5

    with open('grade.json') as fp:
        dictObj = json.load(fp)

    with open('grade.json', 'r+') as file:
        dictObj['grade'].append(grade)
        file.write(json.dumps(dictObj))
        file.close()


if __name__ == "__main__":
    main()
