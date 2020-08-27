print('calculator')
print('enter  1st number')
num1 = input()
print('enter 2nd number')
num2 = input()
print('enter operator')
opt = input()

if opt == '+':
    print(int(num1) + int(num2))
elif opt == '*':
    print(int(num1) * int(num2))
elif opt == '-':
    print(int(num1) - int(num2))
elif opt == '/':
    print(int(num1) / int(num2))
else:
    print('invalid operator')
    
