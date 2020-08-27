def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        return None