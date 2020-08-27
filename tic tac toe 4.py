# PROGRAM FOR TIC TAC TOE
import random
import sys

theBoard = {'topL' : ' ', 'topM' : ' ', 'topR' : ' ', 'midL' : ' ', 'midM' : ' ', 'midR' : ' ', 'lowL' : ' ', 'lowM' : ' ', 'lowR' : ' '}
place = list(theBoard.keys()) #LIST OF POSSIBLE MOVES

def display(board):   #TO DISPLAY THE BOARD
    print((board)['topL'] + '|' + (board)['topM'] + '|' + (board)['topR'] )
    print('-----')
    print((board)['midL'] + '|' + (board)['midM'] + '|' + (board)['midR'] )
    print('-----')
    print((board)['lowL'] + '|' + (board)['lowM'] + '|' + (board)['lowR'], end = '\n\n')

def intro():   #START SCREEN
    global Psign, Csign
    print('' + '    TIC-TAC-TOE')
    display(theBoard)
    print('Choose X or O') #ASSIGNING OF SIGN
    Psign = input()
    pos = ['X', 'O']
    pos.remove(Psign)
    Csign = pos[0]
intro()    

def condn(): #WIN AND LOSE CONDITIONS
    global win, lose, Psign, Csign
    win = Psign == theBoard['topL'] == theBoard['topM'] == theBoard['topR'] or\
          Psign == theBoard['midL'] == theBoard['midM'] == theBoard['midR'] or\
          Psign == theBoard['lowL'] == theBoard['lowM'] == theBoard['lowR'] or\
          Psign == theBoard['topL'] == theBoard['midL'] == theBoard['lowL'] or\
          Psign == theBoard['topM'] == theBoard['midM'] == theBoard['lowM'] or\
          Psign == theBoard['topR'] == theBoard['midR'] == theBoard['lowR'] or\
          Psign == theBoard['topL'] == theBoard['midM'] == theBoard['lowR'] or\
          Psign == theBoard['topR'] == theBoard['midM'] == theBoard['lowL']

    lose = Csign == theBoard['topL'] == theBoard['topM'] == theBoard['topR'] or\
           Csign == theBoard['midL'] == theBoard['midM'] == theBoard['midR'] or\
           Csign == theBoard['lowL'] == theBoard['lowM'] == theBoard['lowR'] or\
           Csign == theBoard['topL'] == theBoard['midL'] == theBoard['lowL'] or\
           Csign == theBoard['topM'] == theBoard['midM'] == theBoard['lowM'] or\
           Csign == theBoard['topR'] == theBoard['midR'] == theBoard['lowR'] or\
           Csign == theBoard['topL'] == theBoard['midM'] == theBoard['lowR'] or\
           Csign == theBoard['topR'] == theBoard['midM'] == theBoard['lowL']
condn()
def game():
    global Psign, Csign, win, lose
    

    
    choice = random.choice(['Cpu', 'You'])  #TO SLECT THE STARTING PLAYER
    print(choice + ' will go first\n')
    if choice == 'Cpu':                     
        


        while win == False and lose == False: #when CPU goes first
            moveC = random.choice(place)
            
            theBoard[(moveC)] = Csign     #CPU MOVE
            display(theBoard)

            place.remove(moveC)    #place.remove is used to remove used positions from possible moves list ie places

            condn()
            if win or lose == True:    #condition check
                continue                      
            
            
            
            print('Choose a Move' + str(place))
            
            
            print('your turn')    

            moveP = input()

            
            theBoard[moveP] = Psign
            display(theBoard)        #PLAYER MOVE

            place.remove(moveP)
            
            condn()
            
            
        if win == True:
            print('Congratulations! You Won')
        elif lose == True:

            print('You Lose')
    elif choice == 'You': #when player goes First
        while win == False and lose == False:
            print('Choose a Move' + str(place))
            moveP = input()
            theBoard[moveP] = Psign
            display(theBoard)                #PLAYER MOVE                        

            place.remove(moveP)    
            condn()      #UPADTING CONDITONS
            if win or lose == True:
                continue                      #condition check
            
            

            moveC = random.choice(place)
                    
            theBoard[(moveC)] = Csign
            display(theBoard)              # CPU MOVE
            place.remove(moveC)
            
            condn()  #UPADTING CONDITONS
            if win or lose == True:       #condition check
                continue

            
            print('your turn')

        if win == True:
            print('Congratulations! You Won')
            print('\nWanna Play again ? (y/n)')
            choice = input()
            if choice == 'y':
                intro()
            elif choice == 'n':
                print('Thank you for playing TIC TAC TOE')
                sys.exit()
            else:
                sys.exit()
        
        elif lose == True:

            print('You Lose')

game()



     
         




        
        
      
        

         
        
    
    
