print('enter name please')
name = input()
if name:
    print('hello ' + name + ' please enter password')
    password = input()
    if (password == name) :
        print('access granted')
    else:
        print('access denied')
else:
    print('you have not entered a name')
    
            

        
