from .Matrix import Matrix

class NeuralNetwork:
	def __init__(self, architecture=[2, 4, 1], lr=0.01):
		self.architecture = architecture
	def __repr__(self):
		return "NeuralNetwork({})".format(self.architecture)
