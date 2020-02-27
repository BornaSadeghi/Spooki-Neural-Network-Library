from nn import *

# sample data with labels
trainData = [([255, 255, 255], 1), ([0,0,0], -1), ([255, 130, 230], 1), ([180, 110, 100], -1), ([181, 223, 212], 1)]
trainEpochs = 1

n = Node(len(trainData[0][0]))

for _ in range(trainEpochs):
    for i,o in trainData:
        print(i, n.predict(normalizeColour(i)))
        n.train(normalizeColour(i), o)

testColour = 0,0,0

print(n.predict(normalizeColour(testColour)))