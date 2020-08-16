
def funkyWay(string):
    new_string = ""
    counter = 0

    for char in string:
        if(counter %2 == 0):
            new_string  += char.upper()
        else:
            new_string += char
        counter += 1
    
    return new_string

if __name__ == "__main__":

    print("funky way:")
    str1 = funkyWay("abcdefghijok")
    print(str1)

    