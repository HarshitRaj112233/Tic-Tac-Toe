# import random
board=["-","-","-","-","-","-","-","-","-"]
game_still_on=True
array=[]
piece=["X","O"]
opted=[]
winner=None
player1=input("Write Player1 name: ")
player2=input("Write Player2 name: ")
turn=player1
choose=None
dict={}
opted2=None
def display_board():
    for row in range(9):    
        if(row==0):
            print (board[row],end=" | ")
            
        elif check_multiple(row):
            print(board[row],end=" | ")
        else:    
            print(board[row])
            print()

def check_multiple(row):
    if (row+1)%3!=0:
        return True

def play_game():
    # Display game
    global player,player1,choose,opted,dict,opted2
    display_board()
    choose=input("What will Player1 choose between (X and O): ")
    player=choose
    opted.append(choose)
    opted2=("".join(i for i in piece if i not in opted))
    dict[choose]=player1
    dict[opted2]=player2

    while game_still_on:

        handle_turn(player)

        check_if_game_over()

        flip_player()

    if winner==player1 or winner==player2:
        print("Winner",winner)
    else:
        print("Game Tied")

def handle_turn(player):
    global array
    position=input("Enter the position from 1:9 ")
    if(position<"1" or position>"9"):
        raise Exception("Number should be between 0 and 9")
    if int(position) in array:
        print(f"Position {position} already chosen")
        handle_turn(player)
        
    else:
        array.append(int(position))
        
        # print(array)
        position=int(position)-1

        board[position]=player
        display_board()
    # computer_position=random.randint(1,9)
    # print(computer_position)
    # board[computer_position]="O"
    # display_board()

def check_if_game_over():

    check_if_win()

    check_if_draw()


def check_if_win():

    global winner

    row_winner=check_rows()
    # print("row",row_winner)
    column_winner=check_columns()
    # print("col",column_winner)
    diagonal_winner=check_diagonal()
    # print("dig",diagonal_winner)

    if row_winner:
       winner=dict[row_winner]
       
    elif column_winner:
       winner=dict[column_winner]
    elif diagonal_winner:
       winner=dict[diagonal_winner]
    else:
       winner=None

    return

def check_rows():
    global game_still_on
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"

    if row_1 or row_2 or row_3:
        game_still_on=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_columns():
    
    global game_still_on
    column_1=board[0]==board[3]==board[6]!="-"
    column_2=board[1]==board[4]==board[7]!="-"
    column_3=board[2]==board[5]==board[8]!="-"

    if column_1 or column_2 or column_3:
        game_still_on=False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    
    global game_still_on
    diagonal_1=board[0]==board[4]==board[8]!="-"
    diagonal_2=board[2]==board[4]==board[6]!="-"

    if diagonal_1 or diagonal_2 :
        game_still_on=False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_draw():
    global game_still_on
    # for i in range(9):
    #     # print(i)
    #     if (board[i]=="-"):
    #         return
    if "-" not in board:
        game_still_on=False
    return 

def flip_player():
    global player,game_still_on,player1,player2,turn,opted,piece
    if( game_still_on):
        if turn==player1:
           player=("".join(i for i in piece if i not in opted))

           turn=player2
           print(f"{player2}'s turn")
        else:
           turn=player1
           player=choose
           print(f"{player1}'s turn")

        return

play_game()
