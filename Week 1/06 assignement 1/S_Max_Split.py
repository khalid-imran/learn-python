"""
Given a balanced string S
 consists of ['R', 'L'] characters. Split it into maximum number of strings such that the new strings are also balanced.

Note:

Balanced strings are those who have equal quantities of 'L' and 'R' characters.
You can not remove or reorder the characters while making the new strings.
Input
Only one line contains a string S
 (2≤|S|≤1000)
 where |S| is the length of the string.

It's guaranteed that S
 consists of only ['L', 'R'] letters, S
 is balanced and |S|
 is even.

Output
Print maximum number of balanced strings then the balanced strings in any order.
"""
val = input()
def max_split():
    maxString = []
    currentString = ''
    Lcount = 0
    Rcount = 0

    for v in val:
        currentString = currentString+v
        if v == "R":
            Rcount = Rcount+1
        if v == "L":
            Lcount = Lcount+1
        if Rcount == Lcount:
            maxString.append(currentString)
            currentString = ''
            Lcount = 0
            Rcount = 0
    print(len(maxString))
    for str in maxString:
        print(str)        

max_split()