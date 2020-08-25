 def concatenate(l1, l2, connector):
	return[word1+connector+word2 for (word1,word2) in zip(l1,l2)]
	
concatenate(['A','B'],['a','b'],'-')
output: ['A-a', 'B-b']