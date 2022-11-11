
#str = input("Input String")

def reverseString(string):

    ind = len(string)-1
    temp =""

    while ind >= 0:
        temp += string[ind]
        ind -= 1

    return temp


reverseString("Hello")


name= "Hello"

print(name[::1])