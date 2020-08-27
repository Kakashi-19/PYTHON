i = 0
lol = []
lmao =[]
a = 0
def swap_case(s):
    string = s.split()
    for a in range(len(string)):
        lol = []
        for i in range(len(list(string[a]))):

            if list(string[a])[i].islower():
                lol.append(list(string[a])[i].upper())
            elif list(string[a])[i].isupper():
                lol.append(list(string[a])[i].lower())
            else:
                lol.append(list(string[a])[i])
        lmao.append(''.join(lol))
    solv = ' '.join(lmao)


    return solv
