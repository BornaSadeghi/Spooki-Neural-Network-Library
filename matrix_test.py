from NeuralNetwork.matrix import Matrix
import unittest

class TestZeros(unittest.TestCase):
    def test_zeros_result(self):
        self.assertEqual(Matrix.zeros(2,3).get2dArray(), Matrix([[0,0,0], [0,0,0]]).get2dArray())
        self.assertEqual(Matrix.zeros(1,1).get2dArray(), Matrix([[0]]).get2dArray())

class TestShape(unittest.TestCase):
    def test_shape_result(self):
        self.assertEqual(Matrix.zeros(2,3).shape(), (2,3))

class TestGet2dArray(unittest.TestCase):
    def test_2d_array(self):
        pass

class TestGetRow(unittest.TestCase):
    def test_get_row(self):
        self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getRow(1), [4,5,6])

class TestGetColumn(unittest.TestCase):
    def test_get_col(self):
        self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getCol(2), [3,6])