from NN.errorfunctions import mean_squared_error
import unittest

# python3 -m unittest errorfunctions_test.py

class TestMeanSquaredError(unittest.TestCase):
    def test_mse(self):
        self.assertEqual(mean_squared_error([0,1,2], [0,1,2]), 0)
        self.assertEqual(mean_squared_error([1,2,3], [2,3,4]), 1)
        self.assertEqual(mean_squared_error([0,1,2,0,1], [5,3,8,4,2]), 16.4)