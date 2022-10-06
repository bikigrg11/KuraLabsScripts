def checkBalance(string):

    length = len(string)
    print(length)

    # check if the number is even if not return false
    if (length % 2) != 0:
        return False
    
    
    for i in range(int(length/2)):
        if string[i] == '{' and string[length-i-1] != "}":
            return False
        elif string[i] == '[' and string[length-i-1] != "]":
            return False
        elif string[i] == '(' and string[length-i-1] != ")":
            return False
        else:
           pass
    return True


print(checkBalance("{[({[(})]})]}"))