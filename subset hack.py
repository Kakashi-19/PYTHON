s = {}
nCases = int(input())
for a in range(nCases):
    for i in range(2):
        nElem = input()
        nSet = input()
        s.setdefault(nElem, nSet)
        s[nElem] = nSet.split()

print(s)



