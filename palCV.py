import copy, re
s = list(input().lower())
ans = []
l = []
def rev(b):
	b.reverse()
	return b
for i in range(0, len(s)):
	l.append(s[i])
	c = copy.deepcopy(l)
	if l == rev(c):
		ans.append(''.join(l))
		l=[]




print(ans)








