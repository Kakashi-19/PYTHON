# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = int(input())
for i in range(lines):
    string = input()
    sample1 = re.compile(r'\s[&]{2}\s')
    a = sample1.sub(' and ', string)
    sample2 = re.compile(r'\s[|]{2}\s')
    b = sample2.sub(' or ', string)
    if ' && ' and ' || ' in string:
        c = a.replace(' || ', ' or ', 2)
        print(c)
    elif ' && ' in string:
        print(a)
    elif ' || ' in string:
        print(b)
    else:
        print(string)




