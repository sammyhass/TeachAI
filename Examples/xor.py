import TeachAI

xs = [[1, 0], [1, 1], [0, 0], [0, 1]] # xs data for xor
ys = [[1], [0], [0], [1]] # ys data for xor

model = TeachAI.NeuralNetwork(2, 4, 1)
model.fit(xs, ys, 0.01, 50000)

for x in xs:
	print("Prediction for {}: {}".format(x, model.predict(x)))