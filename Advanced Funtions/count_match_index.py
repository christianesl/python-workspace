def count_match_index(input):
	count = 0;
	for index,item in enumerate(input):
		if(index == item):
			count +=1
	print (count)
	
	
count_match_index([0,2,2,1,5,5,6,10])	
output: 4

solution:
def count_match_index(L):
	return len([num for count,num in enumerate(L) if num == count])