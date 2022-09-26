from ctypes import sizeof


list = [5,7,1,4]
k = -3
length = len(list)
newlist = []

if k < 0:
    list.reverse()
    flag = True

k = abs(k)

for i in range(length):
    if k == 0:
        newlist.append(0)
    else:
        findSum = 0
        for j in range(k):
            position = j + i + 1
            if position >= length:
                position = abs(length - position)
            print(list[position])
            findSum += list[position]
        newlist.append(findSum)


print(newlist)