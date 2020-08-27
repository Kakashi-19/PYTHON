# guess number game
import random #for generating a random number
import sys #for exiting the program in case of error


def changeName():
    global name
    
    print('Please enter your name ')
    name = input()
    while name == '':
        
        print("You haven't entered a name \n")
        print('Please enter your name')
        name = input()
        
    print('\nHello ' + name + ' ! ')

def game():
    
    
    secretNumber = random.randint(1, 10) #for genertaing a random number and assigning it to the variable secretNumber
    # print('DEBUG: The secret number is ' + str(secretNumber)) #to use in case of checking
    try: #try and except to tackle value errors
        for guessesTaken in range(1,4):
            print('I thought of a number between 1 to 10. Take a guess! ')
            guess = int(input())

            while guess not in range(1,11):   #to deal with guesses that are out of range 
                print('Invalid Guess!, Please guess a number between 1 to 10')
                guess = int(input())

            guessLeft = 3 - guessesTaken

            if guess < secretNumber:
                print('Think of a bigger number \n')
                print('you have ' + str(guessLeft) +' guesses left ')
            elif guess > secretNumber:
                print('Think of a smaller number ')
                print('you have ' + str(guessLeft) +' guesses left ')
            else:
                break

        if guess == secretNumber:
            print('Bingo! ' + name)
            print('You guessed the secret number in only ' + str(guessesTaken) + ' guesses')
            print('\nwanna try again, y/n ? ')
            choice = input()
            if choice == 'y':
                print('wanna change name, yo/no ? ') #option to change name in a game
                namechoice = input()
                if namechoice == 'yo':
                    changeName()
                    game()
                elif namechoice == 'no':
                    game()
                else:
                    print('Inavalid choice, Continuing to game')
                    game()
                    
               
            elif choice == 'n':    
                sys.exit()
            else:
                print('Invalid Choice' )
                sys.exit    
        else:
            print('Better luck next time! \n')
            print('The secret number was ' + str(secretNumber) )
            print('\nwanna try again, y/n ? ')
            choice = input()
            if choice == 'y':
                
                print('wanna change name, y/n ? ') #option to change name in a game
                namechoice = input()
                if namechoice == 'y':
                    changeName()
                    game()
                elif namechoice == 'n':
                    game()
                else:
                    print('Inavalid choice, Continuing to game')
                    game()
                
            elif choice == 'n':    
                sys.exit()
            else:
                print('Invalid Choice' )
                sys.exit  

    except ValueError :
        print('Invalid Guess. ')
        print('\nRestart, y/n ? ')
        choice = input()
        if choice == 'y':
            
            print(' wanna change name, y/n ? ') #option to change name in a game
            namechoice = input()
            if namechoice == 'y':
                changeName()
                game()
            elif namechoice == 'n':
                game()
            else:
                print('Invalid choice, Continuing to game')
                game()
        elif choice == 'n':    
            sys.exit()
        else:
            print('Invalid Choice' )
            sys.exit()
changeName()
game()
        
