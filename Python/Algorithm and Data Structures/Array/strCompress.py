'''
# String Compression

## Problem

Given a string in the form 'AAAABBBBCCCCCDDEEEEaaa' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def compress(str):

    dictResult = {}
    for char in str:
        if char in dictResult:
            dictResult[char] += 1
        else:
            dictResult[char] = 1
    output = ""    
    
    for num in dictResult:
        output += num
        output+=f'{dictResult[num]}'

    print(output)
       


compress("AAAABBBBCCCCCDDEEEEaaaa")