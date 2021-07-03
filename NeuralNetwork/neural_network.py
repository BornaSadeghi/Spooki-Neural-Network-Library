from NeuralNetwork.matrix import Matrix, matrix_product, activation
from NeuralNetwork.activations import sigmoid

class NeuralNetwork:
    def __init__(self, shape=[1]):
        """
        Parameters
        ----------
        shape: list <int>
        The shape of the neural network, where the i-th number is the number of nodes in the i-th layer
        """
        self.shape = shape
        
        self.weights = []

        # Randomly initialized weights
        for i in range (len(shape)-1):
            self.weights.append(Matrix.rand(shape[i+1], shape[i]))
    
    def feedforward (self, x):
        """
        Parameters
        ----------

        x: list <float>
        The input data, a one-dimensional list in which the nth element is fed to the nth node in the input layer
        """

        if len(x) != self.shape[0]:
            raise Exception("Input must be of shape (%d)" % self.shape[0])

        x = Matrix([x])

        # iterate through layers
        for layer_idx in range(len(self.shape)-1):
            x = activation(matrix_product(x, self.weights[layer_idx]), sigmoid)

        return x

    def train(self, x, y):
        """
        Adjust the weights based on input and desired output data.

        Parameters
        ----------

        x: list <float>
        Input data.

        y: list <float>
        Desired output data.
        """
        pass