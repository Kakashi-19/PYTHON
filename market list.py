import sys, os, shelve, shutil, send2trash

#TO START THE LIST

def startlist():  
    global item, note
    print('' + '\n        $$   LIST v1.0    $$') 
    print('\nEnter item to Start Your List')
    item = input()
    note = [item]
    
    print('Add another item, y/n ?')
    choice = input()
    if choice == 'y':
        mklist()
    else:
        menu()

#TO ADD EXTRA ITEMS

def mklist():
    global note
    print('\nEnter item')
    item = input()
    note += [item]
    xen = shelve.open('todolist')
    xen['list'] = note
    print('\nAdd another item, y/n ?')
    choice = input()
    if choice == 'y':
        mklist()
    else:
        menu()

#TO VIE THE LIST

def viewlist():
    global note
    print('' + '        My  List    \n')
    for i in range(len(note)):
        print('\n' + str(i + 1) + '. ' + note[i])
    menu()    

#TO DELETE ITEMS
def delitem():
    global note
    for i in range(len(note)):
        print('\n' + str(i + 1) + '. ' + note[i])
    print('Which item do you want to  delete ?')
    ch = input()
    del note[int(ch) - 1]
    print('Your new list is\n')
    viewlist()
    
#MAIN MENU

def menu():
    
    print('' + '        $$   LIST v1.0    $$\n')   
    print('\n1. Add item')
    print('2. Delete item')
    print('3. View List')
    print('4. Exit\n')
    opt = input()
    if opt == '1':
        mklist()
    elif opt == '3':
        viewlist()
    elif opt == '2':
        delitem()
    else:
        print('Thank You For Using LIST')
        sys.exit()


startlist()



    
    
    

    
    
    
