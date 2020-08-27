string = input()
for i in range(list(string)):
    if list(string)[i].isalpha() or list(string)[i].isdigit() == True:

        if list(string)[i].isalpha():
            print(True)
            if list(string)[i].islower():
                print(True)
            else:
                print(False)
            if list(string)[i].isupper():
                print(True)
            else:
                print(False)
        else:
            print(False)
        if list(string)[i].isdigit():
            print(True)
        else:
            print(False)
    else:
        print(False)


