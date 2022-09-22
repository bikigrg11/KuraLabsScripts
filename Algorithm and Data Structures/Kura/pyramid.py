'''
Read n and generate a pattern given below
Pattern

         1
        1 2
       1 2 3
      1 2 3 4
     1 2 3 ... n

'''

val = int(input("Please enter the value of your N : "))

for i in range(val+1):
    for j in range(val-i):
        print(" ", end = "")
    for j in range(i):
        print((j+1)," ", end = "")
    print()

