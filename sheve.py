import shelve
import os
import send2trash
import shutil
import sys



# TO ADD EXTRA ITEMS
xen = shelve.open('try2')
note =  xen['things']
def mklist():
    global note, item, xen



    print('\nEnter Word')
    item = input()
    note.append(item)
    note.sort(key=str.lower)

    xen['things'] = note

    print('\nAdd another Word, y/n ?')
    choice = input()
    if choice == 'y':
        mklist()
    else:
        menu()



# TO VIEW THE DICTIONARY

def viewlist():
    global note
    print('' + '        My Words    \n')
    note.sort(key=str.lower)
    for i in range(len(note)):
        print('\n' + str(i + 1) + '.) ' + note[i])

    menu()


# TO DELETE WORDS
def delitem():
    try:
        global note
        for i in range(len(note)):
            print('\n' + str(i + 1) + '.) ' + note[i])
        print('Which Word do you want to  delete ?')
        ch = input()
        note.remove(ch)
        print(ch + ' was Deleted\n')
        xen['things'] = note
        menu()
    except ValueError:
        del note[int(ch) - 1]

        xen['things'] = note
        print(note[(ch) - 1] + ' Was Deleted\n')
        menu()

    # MAIN MENU


def menu():
    print('' + '\n        PERSONAL DICTIONARY')
    print('\n1. Add Word')
    print('2. Delete Word')
    print('3. View Dictionary')

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


menu()










