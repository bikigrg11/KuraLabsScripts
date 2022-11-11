
sum = 0
def sumInt(num):

    if (num / 10) < 1:
        return num
    
    return num%10 + sumInt(num//10)
        

sumInteger = sumInt(4321)

print(sumInteger)