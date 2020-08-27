import re

lines = int(input())
code = []
for i in range(lines):
    string = input()
    code.append(string)
total = ' '.join(code)
hexRegex1 = re.compile('(#[0-9A-Fa-f]{3,6});')

a = hexRegex1.findall(total)

d = '\n'.join(a)
print(d)
