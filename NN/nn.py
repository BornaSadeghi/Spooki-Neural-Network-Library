import math, random

def normalizeColour(colour):
    return colour[0]/255, colour[1]/255, colour[2]/255

# Node/Perceptron class

class Node:
    def __init__(self, numInputs, activationFunc=noFunc, learningRate=0.1):
        self.weights = [random.randint(-1,1) for _ in range (numInputs)]
        self.activationFunc = activationFunc
        self.learningRate = learningRate
        self.bias = 1
    
    def predict (self, inputValues):
        weightedSum = 0
        for i in range (len(self.weights)):
            weightedSum += inputValues[i]*self.weights[i]
            
        return self.activationFunc(weightedSum)
    
    def train (self, inputValues, targetValue):
        prediction = self.predict(inputValues)
        error = targetValue-prediction
        
        print("Error: %f\n" % abs(error))
        
        for i in range (len(self.weights)):
            self.weights[i] += error * inputValues[i] * self.learningRate