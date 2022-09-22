'''
## Problem

Given a string of words, reverse all the words. For example:

Given:
    'This is the best'

Return:
    'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

    '  space here'  and 'space here      '
both become:
    'here space'
'''

def rev_word(s):
    # this removes the whitespaces from begining and end of a string
    s1 = s.strip(' ')

    strRev = s1.split()
    strRev = list(strRev)
    strRev.reverse()

    output = " ".join(strRev)
    # output =""
    # # to create a str from the list
    # for str in strRev:
    #     output+= str
    #     output += " "

    print(output)
    return output


str = rev_word(" This is the best ")