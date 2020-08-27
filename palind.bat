@py "C:\Users\vaibhav pratap singh\Desktop\python\palind.py" %*
@py

import sys
wordL = len((sys.argv[0]).lower())
i = -1
revLetter = []
for i in range(-1, -wordL + -1, -1):
    revLetter.append(list((sys.argv[0]).lower())[i])
if (sys.argv[0]).lower() == revLetter:
    print(sys.argv[0] + ' is a Palindrome')
else:
    print(sys.argv[0] + ' is not a Palindrome')
