from nn2 import NeuralNetwork

nn = NeuralNetwork([4,3,6])

# input and output data
x = [1,2,3,4,5]
y = [1,4,9,16,25]

print(nn.feedforward(x))