def d_list(l):
	dictout = {}
	for index,item in enumerate(l):
		dictout[item] = index
	print (dictout)
		
d_list(['a','b','c'])
output: {'a': 0, 'b': 1, 'c': 2}

solution:
def d_list(L):
    return {key:value for value,key in enumerate(L)}