# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
vowelRegex = re.compile(r'[qwrtypsdfghjklzxcvbnm]?([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnm]', re.I)
a = vowelRegex.findall(string)
if a == []:
    print(-1)
else:
    print('\n'.join(a))
