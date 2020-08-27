string = input()
i =0
for i in range(len(list(string))):
    if list(string)[i].isalpha() or list(string)[i].isdigit() == True:
        print(True)
        break
    else:
        if i == len(list(string)) - 1:
            print(False)
        else:
            continue
i = 0
for i in range(len(list(string))):
    if list(string)[i].isalpha():
        print(True)
        break
    else:
        if i == len(list(string)) -1:
            print(False)
        else:
            continue
i = 0
for i in range(len(list(string))):
    if list(string)[i].isdigit():
        print(True)
        break
    else:
        if i == len(list(string)) - 1:
            print(False)
        else:
            continue

i = 0
for i in range(len(list(string))):
    if list(string)[i].islower():
         print(True)
         break
    else:
        if i == len(list(string)) - 1:
            print(False)
        else:
            continue
i = 0
for i in range(len(list(string))):
    if list(string)[i].isupper():
        print(True)
        break
    else:
        if i == len(list(string)) - 1:
            print(False)
        else:
            continue




