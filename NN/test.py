from neural_network import NeuralNetwork

nn = NeuralNetwork([4,3,6])

# input and output matrices
x = [[1,2,3,4]]
y = [1,4,9,16,25]

print(nn.feedforward(x))