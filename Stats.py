import math
def mean(xs):
	tot = 0
	for i in range(len(xs)):
		tot += xs[i]
	return tot/len(xs)

def std(xs):
	av = mean(xs)
	total = 0
	for i in range(len(xs)):
		total += (xs[i] - av)*(xs[i] - av)
	return math.sqrt(1/(len(xs))* total)