
def calcSum(n):

    if n == 0:
        return 0
    else:
        return n + calcSum(n-1)


sum = calcSum(5)

print(sum)