def sum():
    print('enter first number')
    num1 = input()
    num11 = int(num1)
    print('enter second number \n')
    num2 = input()
    num22 = int(num2)
    res = num11 + num22
    print(res)
    print('want to add another number to the result y / n ')
    choice = input()
    while choice == 'y':
        print('enter number')
        num3 = input()
        res = res + int(num3)
        print(res)
        print('want to add another number to the result y / n ')
        choice = input() 

def subtract():
    print('enter first number')
    num1 = input()
    num11 = int(num1)
    print('enter second number')
    num2 = input()
    num22 = int(num2)
    res = num11 - num22
    print(res)
    print('want to subtract another number to the result y / n ')
    choice = input()
    while choice == 'y':
        print('enter number')
        num3 = input()
        res = res - int(num3)
        print(res)
        print('want to subtract another number to the result y / n ')
        choice = input() 

def multiply():
    print('enter first number')
    num1 = input()
    num11 = int(num1)
    print('enter second number')
    num2 = input()
    num22 = int(num2)
    res = num11 * num22
    print(res)
    print('want to multiply another number to the result y / n ')
    choice = input()
    while choice == 'y':
        print('enter number')
        num3 = input()
        res = res * int(num3)
        print(res)
        print('want to multiply another number to the result y / n ')
        choice = input()      
              
def divide():
    print('enter first number')
    num1 = input()
    num11 = int(num1)
    print('enter second number')
    num2 = input()
    num22 = int(num2)
    res = num11 / num22
    print(res)
    print('want to divide another number to the result y / n ')
    choice = input()
    while choice == 'y':
        print('enter number')
        num3 = input()
        res = res / int(num3)
        print(res)
        print('want to divide another number to the result y / n ')
        choice = input() 

    
