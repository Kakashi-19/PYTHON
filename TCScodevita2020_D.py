#GOOD_JOB
n = int(input())
h, b = map(int, input().split())
p = h*b
l = list(map(int, input().split()))
tv = 0
vol = []    #initial total volume
for a in l:
	tv += a*p
for i in range(len(l)):
	mv = 0

	#left adjacents
	for j in range(i, -1, -1):
		if l[j] >= l[i]:
			mv += l[i]*p
		if l[j] < l[i]:
			break

	#right adjacents
	for k in range(i, len(l)):

		if l[k] >= l[i]:
			mv += l[i]*p
		if l[k] < l[i]:
			break
	vol.append(mv - (l[i]*p))   #coz i is counted 2 times

print(tv - max(vol))
