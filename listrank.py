n = int(input())
COM = {}
out = []
def rev(l):
    l.reverse()
    return l
for i in range(n):
    com = input()
    COM.setdefault(i, com.split())
    if 'print' in COM[i]:
        print(out)
    elif 'insert' in COM[i]:
        out.insert(int(COM[i][1]), int(COM[i][2]))
    elif 'remove' in COM[i]:
        out.remove(int(COM[i][1]))
    elif 'append' in COM[i]:
        out.append(int(COM[i][1]))
    elif 'sort' in COM[i]:
        out.sort()
    elif 'pop' in COM[i]:
        out.pop()
    elif 'reverse' in COM[i]:
        out = rev(out)


