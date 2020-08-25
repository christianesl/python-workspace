list1 = = ['hello','are','cat','dog','ham','hi','go','to','heart']
def filter_words(word_list, letter):
	return filter(lambda word: word[0]==letter, word_list)
	
filter_words(list1, 'h')
output: ['hello', 'ham', 'hi', 'heart']