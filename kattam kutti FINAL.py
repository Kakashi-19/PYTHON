# PROGRAM FOR TIC TAC TOE
import random
import sys
import copy

theBoard = {'topL' : ' ', 'topM' : ' ', 'topR' : ' ', 'midL' : ' ', 'midM' : ' ', 'midR' : ' ', 'lowL' : ' ', 'lowM' : ' ', 'lowR' : ' '}
posMove = list(theBoard.keys()) #LIST OF POSSIBLE MOVES
Board2 = copy.deepcopy(theBoard) #CREATED VARIABLE COPY OF COPY OF THEBOARD{}

def display(board):   #TO DISPLAY THE BOARD
    print((board)['topL'] + '|' + (board)['topM'] + '|' + (board)['topR'] )
    print('-+-+-')
    print((board)['midL'] + '|' + (board)['midM'] + '|' + (board)['midR'] )
    print('-+-+-')
    print((board)['lowL'] + '|' + (board)['lowM'] + '|' + (board)['lowR'], end = '\n\n')


def intro(mat):   #START SCREEN
    global Psign, Csign
    print('' + '    KATTAM KUTTI')
    display(mat)
    print('Choose X or O') #ASSIGNING OF SIGN
    Psign = input()
    pos = ['X', 'O']
    pos.remove(Psign)
    Csign = pos[0]
    
    
intro(theBoard)


try:
    def condn(dbc): #WIN AND LOSE CONDITIONS
        global win, lose, Psign, Csign
        win = Psign == dbc['topL'] == dbc['topM'] == dbc['topR'] or\
              Psign == dbc['midL'] == dbc['midM'] == dbc['midR'] or\
              Psign == dbc['lowL'] == dbc['lowM'] == dbc['lowR'] or\
              Psign == dbc['topL'] == dbc['midL'] == dbc['lowL'] or\
              Psign == dbc['topM'] == dbc['midM'] == dbc['lowM'] or\
              Psign == dbc['topR'] == dbc['midR'] == dbc['lowR'] or\
              Psign == dbc['topL'] == dbc['midM'] == dbc['lowR'] or\
              Psign == dbc['topR'] == dbc['midM'] == dbc['lowL']

        lose = Csign == dbc['topL'] == dbc['topM'] == dbc['topR'] or\
               Csign == dbc['midL'] == dbc['midM'] == dbc['midR'] or\
               Csign == dbc['lowL'] == dbc['lowM'] == dbc['lowR'] or\
               Csign == dbc['topL'] == dbc['midL'] == dbc['lowL'] or\
               Csign == dbc['topM'] == dbc['midM'] == dbc['lowM'] or\
               Csign == dbc['topR'] == dbc['midR'] == dbc['lowR'] or\
               Csign == dbc['topL'] == dbc['midM'] == dbc['lowR'] or\
               Csign == dbc['topR'] == dbc['midM'] == dbc['lowL']
    condn(dbc)
except NameError:
    dbc = copy.deepcopy(Board2)
    condn(dbc)
def game(place, db):
    global Psign, Csign, win, lose
    if db != theBoard:
        print('Choose X or O') #ASSIGNING OF SIGN
        Psign = input()
        pos = ['X', 'O']
        pos.remove(Psign)
        Csign = pos[0]
        

    try:
        choice = random.choice(['Cpu', 'You'])  #TO SLECT THE STARTING PLAYER
        print(choice + ' will go first\n')
        if choice == 'Cpu':
            condn(db)
            


            while win == False and lose == False: #when CPU goes first

                moveC = random.choice(place)
                db[(moveC)] = Csign     #CPU MOVE
                display(db)
                place.remove(moveC)    #place.remove is used to remove used positions from possible moves list ie places
                condn(db)

                if win or lose == True:    #condition check
                    continue                      

                print('\nyour turn')
                print('Choose a Move' + str(place))
                moveP = input()
                while db[moveP] != ' ':
                    print('This Position Is already filled')
                    print('Enter valid Move')
                    moveP = input()
                    if moveP == Psign:
                        break
                db[moveP] = Psign
                display(db)        #PLAYER MOVE
                place.remove(moveP)
                condn(db)
                
                
            if win == True:
                print('Congratulations! You Won')
                print('\nWanna Play again ? (y/n)')
                choice = input() #exp
                if choice == 'y':
                    game(copy.deepcopy(posMove), copy.deepcopy(Board2))
                elif choice == 'n':
                    print('\nThank you for playing KATTAM KUTTI')
                    sys.exit()
                else:
                    sys.exit()
            elif lose == True:
                print('You Lose')
                print('\nWanna Play again ? (y/n)')
                choice = input()
                if choice == 'y':
                    game(copy.deepcopy(posMove), copy.deepcopy(Board2))
                elif choice == 'n':
                    print('\nThank you for playing KATTAM KUTTI')
                    sys.exit()
                else:
                    sys.exit()

                
        elif choice == 'You': #when player goes First
            condn(db)
            while win == False and lose == False:
                print('Choose a Move' + str(place))
                moveP = input()
                while db[moveP] != ' ':
                    print('This Position Is already filled')
                    print('Enter valid Move')
                    moveP = input()
                    if moveP == Psign:
                        break
                db[moveP] = Psign
                display(db)                #PLAYER MOVE                        

                place.remove(moveP)    
                condn(db)      #UPADTING CONDITONS
                if win or lose == True:
                    continue                      #condition check
                
                

                moveC = random.choice(place)
                        
                db[(moveC)] = Csign
                display(db)              # CPU MOVE
                place.remove(moveC)
                
                condn(db)  #UPADTING CONDITONS
                if win or lose == True:       #condition check
                    continue

                
                print('your turn')

            if win == True:
                print('*Congratulations! You Won*')
                print('\nWanna Play again ? (y/n)')
                choice = input()
                if choice == 'y':
                    game(copy.deepcopy(posMove), copy.deepcopy(Board2))
                elif choice == 'n':
                    print('\nThank you for playing KATTAM KUTTI')
                    sys.exit()
                else:
                    sys.exit()
            
            elif lose == True:

                print('*You Lose*')
                print('\nWanna Play again ? (y/n)') #to restart the game
                choice = input()
                if choice == 'y':
                    game(copy.deepcopy(posMove), copy.deepcopy(Board2))

                elif choice == 'n':
                    print('\nThank you for playing KATTAM KUTTI')
                    sys.exit()
                else:
                    sys.exit()
    except IndexError:
        
        print('Its a DRAW!')
        print('\nWanna Play again ? (y/n)')
        choice = input()
        if choice == 'y':
            game(copy.deepcopy(posMove), copy.deepcopy(Board2))
        elif choice == 'n':
            print('\nThank you for playing KATTAM KUTTI')
            sys.exit()
        else:
            sys.exit()
game(copy.deepcopy(posMove), theBoard)



     
         




        
        
      
        

         
        
    
    
