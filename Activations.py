import math
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def ReLU(x):
	if x > 0:
		return x
	return 0

def tanh(x):
	return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))