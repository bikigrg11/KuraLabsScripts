def checkPairSum(listNum,sum):
  
    output = []
    temp = []
    for i in listNum:
        subNum = sum - i
        if subNum in listNum:
            temp.append((min(i,subNum),  max(i,subNum)))
    
    print(temp)

    ansDict = list(set(temp))
    return ansDict


num = checkPairSum([1,3,2,2],4)
print(num)