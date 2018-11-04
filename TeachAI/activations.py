import math
from Matrix import Matrix

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def dsigmoid(y):
	return y * (1 - y)


def ReLU(x):
	if x > 0:
		return x
	return 0

def tanh(x):
	return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

def softmax(mat):
	total = 0
	if isinstance(mat, Matrix):
		if mat.cols == 1:
			for i in range(mat.rows):
				total += mat[i][0]
	result = Matrix(mat.rows, 1)
	for i in range(mat.rows):
		result.data[i][0] = mat[i][0] / total
	return result
 