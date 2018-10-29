import math
import random
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

def max(xs):
	maxi = xs[0]
	for i in range(len(xs)):
		if xs[i] > maxi:
			maxi = xs[i]
	return maxi

def argmax(xs):
	maxi = 0
	maxx = xs[0]
	for i in range(len(xs)):
		if xs[i] > maxx:
			maxi = i
			maxx = xs[i]
	return maxi

def scramble(a, b):
	ar = []
	br = []
	if len(a) != len(b):
		Exception("Length of arrays must be the same")
	follow = [i for i in range(len(a))]
	random.shuffle(follow)
	for i in range(len(follow)):
		ar.append(a[follow[i]])
		br.append(b[follow[i]])
	return ar, br

