import re
lines = int(input())
for i in range(lines):
    string = input()
    emRegex = re.compile('''
    [A-Za-z]+
    \s
    <
    [a-zA-Z]
    [a-zA-Z0-9_.-]+ 
    @
    [a-zA-Z]+
    \. 
    [a-zA-Z]{1,3} #domainname
    >
    ''', re.VERBOSE)
    a = emRegex.findall(string)
    if a != []:
        print(a[0])