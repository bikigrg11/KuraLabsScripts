'''
Read n and generate a pattern given below
Pattern

        1
       2 3
      4 5 6
     7 8 9 10

'''

val = int(input("Please enter the value of your N : "))
line = 0
num = 0
for i in range(val+1):
    line+=1
    if(num>val):
        break
    for j in range(val-line):
        print(" ", end="")
    for j in range(line):
        num+=1
        if(num>val):
            break
        print(num," ", end="")
  
    print()
    
    



