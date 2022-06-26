from random import uniform
from neural_network import NeuralNetwork

nn = NeuralNetwork([5,10,5])

# input and output matrices
x = [1,2,3,4,5]
y = [1,4,9,16,25]

nn.feedforward(x)
nn.backpropagate(y)