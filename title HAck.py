
# Complete the solve function below.
a = []
s = input()
new = s.split()
for i in range(len(new)):
    if new[i].isalnum() == True:
        if list(new[i])[0].isdigit() == True:
            a.append(new[i])
        else:
            new[i].title()
            a.append(new[i].title())
    else:
        d = new[i].title()
        a.append(d)
c = ' '.join(a)
print(c)






