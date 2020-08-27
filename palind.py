import sys
a = sys.argv
wordL = len(a[1])

revLetter = []
for i in range(-1, -wordL + -1, -1):
    revLetter.append(list(a[1].lower())[i])
if list((a[1]).lower()) == revLetter:
    print(a[1] + ' is a Palindrome')
else:
    print(a[1] + ' is not a Palindrome')