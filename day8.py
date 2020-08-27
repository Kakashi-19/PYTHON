import sys

n = int(input())
logs = {}
for i in range(n):
    data = input().split()
    logs.setdefault(data[0], data[1])

while True:
    name = sys.stdin.readline().strip()      #tolearn
    if name in logs.keys():
        print(name + '=' + logs[name])
    elif name == '':
        break
    else:
        print('Not found')

