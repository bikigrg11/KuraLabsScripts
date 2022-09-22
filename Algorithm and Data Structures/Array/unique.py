import collections

def checkUnique(str1):
    check = collections.defaultdict(int) 

    for ch in str1:
        check[ch] += 1
    
    for ch in str1:
        if check[ch] > 1:
            print(ch + " is repeated")
            return ch 
    print("Nothing is repeated")

checkUnique("abcde")