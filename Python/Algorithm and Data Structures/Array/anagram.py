def checkAnagram(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if(len(str1) != len(str2)):
        print("Strings are not equal")
        return -1
    
    string1 = ''.join(sorted(str1))
    string2 = ''.join(sorted(str1))
    
    sortStr1 = str(string1)
    sortStr2 = str(string2)

    if sortStr1 == sortStr2:
        print("Strings are equal")
        return 0
    else:
        print("Strings are not equal")
        return -1

str1 = "publics relations"
str2 = "crap buit on lies"

def checkAnagram2(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if len(str1) != len(str2) :
        print("Strings are not equal")
        return -1
    
    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        
    for letter in str2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1
        
        # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False



    print("same")

str1 = "public relations"
str2 = "crap built on lies"

a ="abc"
b ="cda"
checkAnagram2(a,b)
