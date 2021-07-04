import math

def linear (x):
    return x

def reLU (x):
    return max(0,x)

def sigmoid (x):
    return 1/(1+math.e**-x)

def sign(x):
    return 1 if x >= 0 else -1