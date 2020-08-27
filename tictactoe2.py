# PROGRAM FOR TIC TAC TOE
import random
import sys

theBoard = {'topL' : ' ', 'topM' : ' ', 'topR' : ' ', 'midL' : ' ', 'midM' : ' ', 'midR' : ' ', 'lowL' : ' ', 'lowM' : ' ', 'lowR' : ' '}
place = list(theBoard.keys())

def display(board):
    print((board)['topL'] + '|' + (board)['topM'] + '|' + (board)['topR'] )
    print('-----')
    print((board)['midL'] + '|' + (board)['midM'] + '|' + (board)['midR'] )
    print('-----')
    print((board)['lowL'] + '|' + (board)['lowM'] + '|' + (board)['lowR'] )

print('' + '    TIC-TAC-TOE')
display(theBoard)
print('Choose X or O')
Psign = input()
pos = ['X', 'O']
pos.remove(Psign)
Csign = pos[0]    



def condition():
    global win, lose
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
    
def game():
    global Psign, Csign, win, lose
    
    choice = random.choice(['Cpu', 'You'])  #TO SLECT THE STARTING PLAYER
    print(choice + ' will go first')
    if choice == 'Cpu':              #CPU MOVE
        while win and lose == False:
            moveC = random.choice(place)
            
            theBoard[(moveC)] = Csign
            display(theBoard)
            place.remove(moveC)
            print('Choose a Move' + str(place))
            
            
            print('your turn')    #PLAYERMOVE
            moveP = input()
            theBoard[moveP] = Psign
            display(theBoard)
            place.remove(moveP)
            condition()
        if win == True:
            print('Congratulations! You Won')
        elif lose == True:

            print('You Lose')

condition()




        
        
      
        

         
        
    
    
