array = [0,0,0,0,0,0,0,0,0,0]

num = [2,1,4,3,5]

for i in num:
    array[i] += 1


output = []

for i in range(1,len(array)):
    if array[i] == 1:
        output.append(i)

print(output)