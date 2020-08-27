# input
n = int(input())
query = []

for i in range(n):
    s = input()
    x = int(input())
    query.append((s, x))
w = []
b = []

print(query)
for a in query:
    for i in range(len(a[0])):
        w.append(0)
    b.append(w)
# check    //a[0] = s, a[1] = x
c = 0
for a in query:
	w = b[c]
    for i in range(len(a[0])):

        if i + 1 > a[1]:
            if int(a[0][i]) == 1:
                w[i - a[1]] = 1  # i - x
            if int(a[0][i]) == 0:
                w[i - a[1]] = 0

        if i + 1 + (a[1]) <= len(a[0]):
            if int(a[0][i]) == 1:
                w[i + a[1]] = 1

            if int(a[0][i]) == 0:
                w[i + a[1]] = 0
    c += 1
# apply


# output
