from unittest.case import TestCase
from NN.matrix import Matrix, dot, matrix_product
import unittest

# python3 -m unittest matrix_test.py

class TestInit(unittest.TestCase):
    def test_invalid_shape(self):
        with self.assertRaises(Exception):
            Matrix([1,2,3])
        with self.assertRaises(Exception):
            Matrix([]) 
    def test_empty_row_or_column(self):
        with self.assertRaises(Exception):
            Matrix([[]])
    def test_uneven_row_length(self):
        with self.assertRaises(Exception):
            Matrix([[1,2,3], [4,5]])
        with self.assertRaises(Exception):
            Matrix([[], [1,2,3]])

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

class TestDot(unittest.TestCase):
    def test_dot_product(self):
        self.assertEqual(dot([1,2,3], [4,5,6]), 32)
        self.assertEqual(dot([1,0,-1], [1,1,1]), 0)
    
    def test_different_lengths(self):
        with self.assertRaises(Exception):
            dot([0,1], [2,3,4])

class TestMatrixMultiplication(unittest.TestCase):
    def test_mat_mul(self):
        self.assertEqual( matrix_product(Matrix([[1,2], [3,4], [5,6]]), Matrix([[1,0,0], [2,1,3]])).get2dArray(), [[5,2,6], [11,4,12], [17,6,18]] )
        self.assertEqual( matrix_product(Matrix([[2, -3, 0, 4]]), Matrix([[2],[4],[5],[-3]])).get2dArray(), [[-20]] ) 

class TestTranspose(unittest.TestCase):
    def test_transpose_result(self):
        self.assertEqual( Matrix([[2,3], [4,5]]).transpose().get2dArray(), [[2,4], [3,5]])