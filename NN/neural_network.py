from matrix import Matrix, matrix_product, activation
from activations import sigmoid

class NeuralNetwork:
    def __init__(self, shape=[1]):
        """
        Parameters
        ----------
        shape: list <int>
            The shape of the neural network, where the i-th number is the number of nodes in the i-th layer
        ----------
        """
        self.shape = shape
        
        # List of n matrices, where n is the number of layers
        self.weights = []

        # Randomly initialized weights for each layer
        for i in range (len(shape)-1):
            self.weights.append(Matrix.rand(shape[i+1], shape[i]))
    
    def feedforward (self, x):
        """
        Parameters
        ----------
        x: list <float>
            The input data, a one-dimensional list in which the nth element is fed to the nth node in the input layer
        ----------

        TODO
        Fix documentation, as x is not a one-dimensional list
        Alternatively, make x have to be a one-dimensional list
        """

        assert len(x[0]) == self.shape[0], "Input layer must be of shape (1, %d)" % self.shape[0]

        x = Matrix(x).transpose()

        # iterate through layers
        for layer_idx in range(len(self.shape)-1):
            x = activation(matrix_product(self.weights[layer_idx], x), sigmoid)

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
        ----------
        """
        pass