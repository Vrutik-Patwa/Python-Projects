print("Welcome to TIC-TAC-TOE")



def display_board(board):
    print("  |   |")
    print(board[1]+' | '+board[2]+' | '+board[3])
    print("  |   |")
    print("-"*10)
    print("  |   |")
    print(board[4]+' | '+board[5]+' | '+board[6])
    print("  |   |")
    print("-"*10)
    print("  |   |")
    print(board[7]+' | '+board[8]+' | '+board[9])
    print("  |   |")

# display_board(test_board)

def player_input():

    marker = ''

    while marker != 'X' and marker!='O':
        marker = input('Player 1 choose X or O : ').upper()

    if marker =='X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):

    board[position] = marker

def win_check(board,mark):

    #straight line in rows
    for i in range(1,8,3):
        if(board[i]==mark and board[i+1]==mark and board[i+2]==mark):
           
            return True

    #straight line in columns
    for i in range(1,4):
        if(board[i]==mark and board[i+3]==mark and board[i+6]==mark):
            
            return True
    
    #diagonal rows
    if(all(board[i] == mark for i in range(1,10,4))) or all(board[i] == mark for i in range(3,8,2)):
        
        return True
    
    return False


def space_check(board,position):
    
    return (board[position]==' ')
        
def full_board_check(board):
    
    for position in range(1,10):
        if(space_check(board,position)):
            return True
    return False

def player_choice(board):
    while True:
        position = int(input('Choose a position : (1-9) : '))
        
        if(position not in list(range(1,10))):
            print("Choose a valid num")
        elif(not space_check(board,position)):
            print("Already taken")
        else:
            return position
    

def Player_turn():
    turn = random.randint(0,1)

    return turn

def replay():
    game = input("for replay press 'Y' and for exit press any other key :" ).lower()

    if game == 'y':
        return True

    return False

while(True):
    board = [' ']*10
    display_board(board)
    #turn = Player_turn()
    player1,player2 =player_input()
    # if(turn):
    while(full_board_check(board)):
        index = player_choice(board)
        place_marker(board,player1,index)
        display_board(board)
        if(win_check(board,player1)):
            print("Player 1 Won")
            break
        index = player_choice(board)
        place_marker(board,player2,index)
        display_board(board)
        if(win_check(board,player2)):
            print("Player 2 Won")
            break
    else:
        print("its a tie")
    if(not replay()):
        
        break

    
   


