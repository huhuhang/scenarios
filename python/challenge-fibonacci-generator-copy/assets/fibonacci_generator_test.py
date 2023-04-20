import sys
sys.path.append("/home/labex/project")

import unittest
from fibonacci_generator import fibonacci_generator

class TestFibonacciGenerator(unittest.TestCase):
    def test_fibonacci_generator(self):
        fibonacci_gen = fibonacci_generator(5)
        result = list(fibonacci_gen)
        self.assertEqual(result, [0, 1, 1, 2, 3])

        fibonacci_gen = fibonacci_generator(10)
        result = list(fibonacci_gen)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

        fibonacci_gen = fibonacci_generator(1)
        result = list(fibonacci_gen)
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()