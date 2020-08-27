k = int(input())
roomL = input()
counter = {}
for i in roomL.split():
    counter.setdefault(i, 0)
    counter[i] += 1
cl = list(counter.values())
new = list(counter.keys())
print(new[cl.index(1)])


