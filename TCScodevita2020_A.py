import re

length = int(input())
txt = input()

va = 0
vb = 0
vc = 0

txtRegexA = re.compile(r'[-]*A')
a = txtRegexA.findall(txt)

txtRegexB = re.compile(r'B[-]*')
b = txtRegexB.findall(txt)

txtRegexN = re.compile(r'B[-]+A')
c = txtRegexN.findall(txt)

for i in a:
	va += len(i)

for j in b:
	vb += len(j)

for k in c:
	vc += len(k)

n = (vc - 1*len(c))//2

if va - n > vb - n:
	print('A', end='')
elif va - n < vb - n:
	print('B', end='')
else:
	print('Coalition government', end='')
