def reverseString(str1):

    if str1 == "":
        return ""
    else:
        newStr = reverseString(str1[1:]) + str1[0] 
        return  newStr

    
str = "biki"
print(reverseString(str))
