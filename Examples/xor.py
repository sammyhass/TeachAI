import TeachAI

xs = [[1, 0], [1, 1], [0, 0], [0, 1]] # xs data for xor
ys = [[1], [0], [0], [1]] # ys data for xor

model = TeachAI.NeuralNetwork(2, 10, 1) # create neural net with architecture 2 input nodes, 10 hidden nodes and 1 output node
model.fit(xs, ys, 1, 1000) # fit the model with learning rate of 1 and run over 1000 epochs
for x in xs: 
	print("Prediction for {}: {}".format(x, model.predict(x)))
