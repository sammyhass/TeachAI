from .Matrix import Matrix
from . import Activations
class NeuralNetwork:
	def __init__(self, architecture=[2, 4, 2], lr=0.01):
		self.architecture = architecture
		self.ih = Matrix(self.architecture[1], self.architecture[0])
		self.ih.randomize_dec()
		self.ho = Matrix(self.architecture[2], self.architecture[1])
		self.ho.randomize_dec()

	def __repr__(self):
		return "NeuralNetwork({})".format(self.architecture)

	def predict(self, inputs):
		input_matrix = Matrix(self.architecture[0], 1, data=inputs)
		hidden_matrix = Matrix.matMul(self.ih, input_matrix)
		hidden_matrix_activation = Matrix.apply(hidden_matrix, Activations.sigmoid)
		output_matrix = Matrix.matMul(self.ho, hidden_matrix_activation)
		prediction = Matrix.apply(output_matrix, Activations.sigmoid)
		return prediction.data

	def fit(self, xs, ys, lr):
		for i in range(len(xs)):
			print("{}/{}".format(i+1, len(xs)))
			input_matrix = Matrix(self.architecture[0], 1, data=xs[i])
			hidden_matrix = Matrix.matMul(self.ih, input_matrix)
			hidden_activation = Matrix.apply(hidden_matrix, Activations.sigmoid)
			output_matrix = Matrix.matMul(self.ho, hidden_activation)
			outputs = Matrix.apply(output_matrix, Activations.sigmoid)
			target_matrix = Matrix(self.architecture[2], 1, data=ys[i])
			output_errors = Matrix.sub(target_matrix, outputs)
			gradients = Matrix.apply(outputs, Activations.sigmoid)
			gradients = Matrix.mul(gradients, output_errors)

			gradients = Matrix.mul(gradients, lr)

			hidden_T = Matrix.transpose(hidden_activation)
			weight_ho_deltas = Matrix.matMul(gradients, hidden_T);
			self.ho = Matrix.add(self.ho, weight_ho_deltas)

			who_t = Matrix.transpose(self.ho)
			hidden_errors = Matrix.matMul(who_t, output_errors)

			hidden_gradient = Matrix.apply(hidden_activation, Activations.sigmoid)

			hidden_gradient = Matrix.mul(hidden_gradient, hidden_errors)
			hidden_gradient = Matrix.mul(hidden_gradient, lr)

			inputs_T = Matrix.transpose(input_matrix)
			weight_ih_deltas = Matrix.matMul(hidden_gradient, inputs_T)
			self.ih = Matrix.add(self.ih, weight_ih_deltas)






