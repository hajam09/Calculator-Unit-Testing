import unittest
import Calculator
import random


class TestCalculator(unittest.TestCase):

    def test_add(self):
        for i in range(100):
            x = random.randint(-9999, 9999)
            y = random.randint(-9999, 9999)
            self.assertEqual(Calculator.add(x,y), x+y)

    def test_subtract(self):
        for i in range(100):
            x = random.randint(-9999, 9999)
            y = random.randint(-9999, 9999)
            self.assertEqual(Calculator.subtract(x,y), x-y)

    def test_multiply(self):
        for i in range(100):
            x = random.randint(-9999, 9999)
            y = random.randint(-9999, 9999)
            self.assertEqual(Calculator.multiply(x,y), x*y)

    def test_divide(self):
        for i in range(100):
            x = random.randint(-9999, 9999)
            y = random.randint(-9999, 9999)
            self.assertEqual(Calculator.divide(x,y), x/y)
            
if __name__=="__main__":
    unittest.main()
