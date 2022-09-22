def translate(string):

    output = []

    for ch in string:       
        
        numVal = ord(ch)
        output.append(numVal)
      
    str2 = ""
    for num in output:
        str2+=str(num)
        
    return str2


str1 = input("Please enter the word you would like to translate:")

print(translate(str1))