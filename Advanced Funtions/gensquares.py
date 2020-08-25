def gensquares(n):
	for num in range(n):
		yield num*num

for x in gensquares(10):
	print x