import unittest 
import calc 

class TestMath(unittest.TestCase): 

    def test_add(self): 
        self.assertEqual(calc.add(6, 5), 13)
        self.assertEqual(calc.add(6, 7), 13)
        self.assertEqual(calc.add(9, 9), 18)
        self.assertEqual(calc.add(6, 4), 10)
        self.assertEqual(calc.add(6, 5), 11)
        self.assertEqual(calc.add(6, 5), 23)
        self.assertEqual(calc.add(6, 3), 9)
    
    def test_subtract(self): 
        self.assertEqual(calc.subtract(6, 5), 1)
        self.assertEqual(calc.subtract(6, 7), -1)
        self.assertEqual(calc.subtract(9, 9), 0)
        self.assertEqual(calc.subtract(6, 4), 2)
        self.assertEqual(calc.subtract(6, 5), 1)
        self.assertEqual(calc.subtract(6, 2), 4)
        self.assertEqual(calc.subtract(6, 3), 3)

    def test_multiply(self): 
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(6, 3), 18)
        self.assertEqual(calc.multiply(9, 9), 81)
        self.assertEqual(calc.multiply(6, 4), 24)
        self.assertEqual(calc.multiply(6, 5), 30)
        self.assertEqual(calc.mulltiply(6, 5), 23)
        self.assertEqual(calc.multiply(6, 3), 9)

    def test_divide(self): 
        self.assertEqual(calc.divide(8, 2), 4)
        self.assertEqual(calc.divide(6, 6), 1)
        self.assertEqual(calc.divide(9, 9), 1)
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(6, 5), 11)
        self.assertEqual(calc.divide(6, 5), 23)
        self.assertEqual(calc.divide(6, 3), 9)

        self.asserrtRaise(ValueError, calc.divide, 10, 0)



if __name__ == '__main__': 
    unittest.main()
