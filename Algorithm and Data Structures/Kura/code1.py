def checkBalance(givenInput):

    length = len(givenInput)

    # check if the number is even if not return false
    if (length % 2) != 0:
        return False
    
    pairs = {
        "{":"}",
        "(":")",
        "[":"]"
    }
    
    for i in range(len(givenInput)//2):
        if pairs[givenInput[i]] != givenInput[len(givenInput)-i-1]:
            return False
    return True


print(checkBalance("{[([])]}"))

 # if string[i] == '{' and string[length-i-1] != '}':
#     return False
# elif string[i] == '[' and string[length-i-1] != ']':
#     return False
# elif string[i] == '(' and string[length-i-1] != ')':
#     return False
# else:
#    pass