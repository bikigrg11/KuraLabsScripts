def freqAlphabets(s):
    
    num =[]
    index = 0

    while index < len(s):
        charNum = ""
        charVal = ''

        if(index+2 < len(s)):
            if s[index+2] == '#' :
                charNum += s[index]
                charNum += s[index+1]
                index += 3
            else:
                charNum += s[index]
                index += 1
            intNum = int(charNum)
            num.append(intNum)
          
        else:
            charNum += s[index]
            index += 1
            intNum = int(charNum)
            num.append(intNum)

    output = ""

    for number in num:
        char = chr(number + 96)
        output += str(char)
    return output


print(freqAlphabets("10#11#12"))