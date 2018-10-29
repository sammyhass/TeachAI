from .Matrix import Matrix
from . import activations
from . import stats

class NeuralNetwork:

	def __init__(self, input_nodes, hidden_nodes, output_nodes):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes

		self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
		self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
		self.weights_ih.randomize()
		self.weights_ho.randomize()

		self.bias_h = Matrix(self.hidden_nodes, 1)
		self.bias_o = Matrix(self.output_nodes, 1)
		self.bias_h.randomize()
		self.bias_o.randomize()

	def predict(self, input_list):
		inputs = Matrix.from_list(input_list)
		hidden = Matrix.multiply(self.weights_ih, inputs)
		hidden.add(self.bias_h)
		hidden.map(Activations.sigmoid)

		output = Matrix.multiply(self.weights_ho, hidden)
		output.add(self.bias_o)
		output.map(Activations.sigmoid)
		return output.to_list()

	def fit(self, xs, ys, lr=0.01, epochs=10):
		for epoch in range(epochs):
			xs, ys = Stats.scramble(xs, ys)
			print("Training, {}/{}".format(epoch+1, epochs))
			for i in range(len(xs)):
				inputs = Matrix.from_list(xs[i])
				hidden = Matrix.multiply(self.weights_ih, inputs)
				hidden.add(self.bias_h)
				hidden.map(Activations.sigmoid)

				outputs = Matrix.multiply(self.weights_ho, hidden)
				outputs.add(self.bias_o)
				outputs.map(Activations.sigmoid)

				targets = Matrix.from_list(ys[i])
				output_errors = Matrix.subtract(targets, outputs)
				gradients = Matrix.map_s(outputs, Activations.dsigmoid)
				gradients.mul(output_errors)
				gradients.mul(lr)

				hidden_T = Matrix.transpose(hidden)
				weights_ho_deltas = Matrix.multiply(gradients, hidden_T)

				self.weights_ho.add(weights_ho_deltas)	
				self.bias_o.add(gradients)	

				who_t = Matrix.transpose(self.weights_ho)  
				hidden_errors = Matrix.multiply(who_t, output_errors)

				hidden_gradient = Matrix.map_s(hidden, Activations.dsigmoid)

				hidden_gradient.mul(hidden_errors)
				hidden_gradient.mul(lr)

				inputs_T = Matrix.transpose(inputs)
				weights_ih_deltas = Matrix.multiply(hidden_gradient, inputs_T)

				self.weights_ih.add(weights_ih_deltas)
				self.bias_h.add(hidden_gradient)	




