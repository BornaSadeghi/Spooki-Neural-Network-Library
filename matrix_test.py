from NeuralNetwork.matrix import Matrix
import unittest

class TestZeros(unittest.TestCase):
    def test_zeros_matrix(self):
        self.assertEqual(Matrix.zeros(2,3).get2dArray(), Matrix([[0,0,0], [0,0,0]]).get2dArray())
        self.assertEqual(Matrix.zeros(1,1).get2dArray(), Matrix([[0]]).get2dArray())