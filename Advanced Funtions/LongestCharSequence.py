def method(input):
    charS = ''
    previous = ''
    maxS = 0
    dict1 = {}
    for itr in input:
        if(previous == itr):
            dict1[itr] = dict1[itr] + 1
            if(dict1[char] > maxS):
                maxS = dict1[char]
                charS = char
        else:
            dict1.clear()
            dict1 = {itr, 1}
            previous = dict1
    print(charS*maxS)


my_string = 'aaabbddkwobkkkkkkdfasdnb'
method(my_string)
