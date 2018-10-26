class LinearRegressor:
	def __repr__(self):
		return "TeachAI.LinearRegressor()"
		self.m = 0
		self.b = 0
	def fit(self, xs, ys):
		sum_x = 0
		sum_y = 0
		if len(xs) != len(ys):	
			raise Exception("Number of xs must be the same as number of ys")
		for i in range(len(xs)):
			sum_x += xs[i]
			sum_y += ys[i]

		mean_x = sum_x / len(xs)
		mean_y = sum_y / len(ys)

		num = 0
		den = 0
		for i in range(len(xs)):
			num += (xs[i] - mean_x) * (ys[i] - mean_y)
			den += (xs[i] - mean_x) * (xs[i]- mean_x)

		m = num / den
		b = mean_y - m * mean_x
		self.m = m
		self.b = b
		return [m, b]

	def predict(self, x):
		return self.m * x + self.b