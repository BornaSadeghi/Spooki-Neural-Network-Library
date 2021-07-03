from NeuralNetwork.neural_network import NeuralNetwork
from NeuralNetwork.neural_network import NeuralNetwork
import unittest

# python3 -m unittest neural_network_test.py

class TestFeedforward(unittest.TestCase):
    def test_input_layer_shape(self):
        # Wrong shape for x; should raise exception
        with self.assertRaises(Exception):
            NeuralNetwork([4,3,6]).feedforward([1,2,3,4,5])