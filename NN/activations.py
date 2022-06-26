import math

def linear (x):
    return x

def reLU (x):
    return max(0,x)

def sigmoid (x):
    return 1/(1+math.e**-x)

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

def sigmoid_inverse(x):
    return -math.log(1/x - 1)

def sign(x):
    return 1 if x >= 0 else -1