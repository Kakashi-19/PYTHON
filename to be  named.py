string = input()
sub_string = input()
import re

def count_substring(string, sub_string, ):


    global t
    sampleRegex = re.compile((sub_string))
    s = sampleRegex.findall(string)
    d = []
    a = sub_string[0]
    b = sub_string[1:]
    i = 1
    while i != 25:
        d.append(a + b*i)

        sampleRegex2 = re.compile(d[i])
        t = sampleRegex2.findall(string)
        i = i + 1
    u = len(t) + len(s)
    return u

print(count_substring(string, sub_string))