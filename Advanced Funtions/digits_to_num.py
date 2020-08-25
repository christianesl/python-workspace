list1 = [3,4,3,2,1]
def digits_to_num(digits):
    return reduce(lambda x,y: x*10+y, digits)
    
output: 34321