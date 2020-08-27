import pprint
word = input()
a = {}
for i in word:
	a.setdefault(i, 0)
	a[i] += 1
pprint.pprint(a)
