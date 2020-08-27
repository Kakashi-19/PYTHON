import copy, sys

n = int(input())
marks = []
names = []
new = []
a = 0
for i in range(n):
    name = input()
    names.append(name)
    mark = float(input())
    marks.append(mark)

newmarks = copy.deepcopy(marks)
newmarks.sort()
if newmarks[0] == newmarks[1]:
    while newmarks[0] == newmarks[1]:

        newmarks.remove(newmarks[0])
        if newmarks[1] == '':
            print(names[marks.index(newmarks[0])])

else:
    if newmarks[a + 1] == newmarks[a + 2]:
        while newmarks[a + 1] == newmarks[a + 2]:
            m1 = marks.index(newmarks[a + 1])
            new.append(names[m1])
            marks.remove(marks[m1])
            names.remove(names[m1])
            m2 = marks.index(newmarks[a + 1])
            new.append(names[m2])
            newmarks.remove(newmarks[a + 1])
            new.sort()
            print(new[a])
            print(new[a + 1])
            a += 1
    else:
        m3 = marks.index(newmarks[1])
        print(names[m3])