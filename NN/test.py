from random import uniform
from neural_network import NeuralNetwork

nn = NeuralNetwork([2,3,3])

# input and output matrices
x = [0, 0]
y = [1,4,9,16,25]

print(x)
print(nn.weights)

print(nn.feedforward(x))