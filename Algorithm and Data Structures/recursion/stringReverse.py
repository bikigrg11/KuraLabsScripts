def reverseString(str):
    
    if str == "":
        return str
    
    subWord = str[1:]
    newWord  = reverseString(subWord)
    newWord = subWord + str[0]
    return newWord

print(reverseString("Hello"))