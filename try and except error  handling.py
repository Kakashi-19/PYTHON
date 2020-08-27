print('how many cats do you have ?')
numcats = input()
try: # how the program will run normally
    if int(numcats) >= 4:
        print('that is a lot of cats')
    elif int(numcats) < 0: #to prevent entering of negative numbers
        
        print('cats cant be negative')
    else:
        print('that is not a lot of cats')
except ValueError: # how the program will behave in case of a value error
                   #value error example int(string without a numeric value i.e have an alphabetical value)
                   # a value error occurs when a wrong type of value is tried to be converted      
    print('you did not enter a number')
