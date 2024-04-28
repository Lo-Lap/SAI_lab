import unittest
import time
from game.GameField import GameField
from play.Optimizer import Optimizer


class ResultTest(unittest.TestCase):
    ANSI_GREEN = "\033[32m"
    FIELD_FILENAME = "fieldFiles/field.csv"
    TIMEOUT_SECONDS = 50

    def test_result(self):
        field = GameField()
        field.fill(self.FIELD_FILENAME)

        # Python's unittest doesn't support a direct timeout on test cases in the same way JUnit does,
        # so we simulate it with a timing check around the potentially slow code.
        start_time = time.time()
        try:
            best_chromosome = Optimizer.optimize(field)
            result = field.testAnt(best_chromosome)
            print(self.ANSI_GREEN + "Your result is " + str(result))
            print(self.ANSI_GREEN + "Max is 89")
        except Exception as e:
            print(f"Error during optimization: {e}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.assertLessEqual(elapsed_time, self.TIMEOUT_SECONDS, "Test exceeded time limit.")


if __name__ == 'main':
    unittest.main()
