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
        
        self.weights = []
        self.biases = []
        self.outputs = [None for _ in range(len(shape))]

        # Randomly initialized weights
        for i in range (len(shape)-1):
            self.weights.append(Matrix.rand(shape[i+1], shape[i]))
            self.biases.append(Matrix.rand(shape[i+1], shape[i]))
    
    def feedforward (self, x):
        """
        Parameters
        ----------
        x: list <float>
            The input data, a one-dimensional list in which the nth element is fed to the nth node in the input layer
        ----------
        """

        assert len(x) == self.shape[0], "Input must be of shape (1, %d)" % self.shape[0]

        # Turn x into an input layer matrix and transpose it to fit the network
        self.outputs[0] = Matrix([x]).transpose()

        # iterate through layers
        for layer_idx in range(len(self.shape)-1):
            self.outputs[layer_idx+1] = activation(matrix_product(self.weights[layer_idx], self.outputs[layer_idx]), sigmoid)

        return self.outputs

    def backpropagate(self, y):
        """
        Parameters
        ----------
        y: list <float>
            The expected output of the neural network.
        ----------
        """
        pass

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