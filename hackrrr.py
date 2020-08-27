# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

i = int(input())
for a in range(i):
    string = input()
    floatRegex = re.compile(r'^(\+?|-?)\d*\.\d+$')
    b = floatRegex.findall(string)
    if b != []:
        print(True)

    else:
        print(False)

