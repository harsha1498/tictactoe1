import random

board=[
                "_", "_", "_",
                "_", "_", "_",
                "_", "_", "_"
            ]
gamerunning= True
player="X"
winner = None
#printboard

def print_board(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

#userinput

def user_inp(board):
        choice=int(input("enter the row :"))
        if board[choice-1]== "_" and choice<=9 and choice>=1:
            board[choice-1]= player
        else:
            print("  opps!! you  selected had"
                  " already placed!")
#horizontal

def horizontal(board):
    global winner
    if board[0] == board[1] == board[2] != "_":
        winner = board[0]
        #print_board(board)
        return True
    elif board[3]==board[4]==board[5] != "_":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] != "_":
        winner = board[6]
        return True
#vertical

def vertical(board):
    global winner
    if board[0]==board[3]==board[6] != "_":
        winner = board[0]
        return True
    elif board[1]==board[4]==board[7] != "_":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] != "_":
        winner = board[2]
        return True
#diagnol

def diagnol(board):
    global winner
    if board[0]==board[4]==board[8] != "_" :
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] != "_" :
        winner = board[2]
        return True


#check wiiner

def check(board):
    global winner
    global gamerunning
    if horizontal(board) is True:
        print_board(board)
        print("winner is {}:".format(winner))
        gamerunning = False
    elif vertical(board) is True:
        print_board(board)
        print("winner is {}:".format(winner))
        gamerunning = False
    elif diagnol(board) is True:
        print_board(board)
        print("winner is {}:".format(winner))
        gamerunning = False
def switch():
    global player
    if player=="X":
        player="O"
        print("now its {} turn".format(player))
    else:
        player="X"

        if gamerunning is False:
            print("<<<<<<<<<<<<<<<<<<<<<<<game over>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print("now its {} turn".format(player))
def tie(board):
    global gamerunning
    if  board[0]!="_" and board[1]!="_" and  board[2]!="_" and board[3]!="_" and  board[4]!="_" and board[5]!="_" and  board[6]!="_" and board[7]!= "_" and  board[8]!="_":
        print(">>>>>>>>>>>>>>game is tie!!!!<<<<<<<<<<<<<<<<<<")
        gamerunning = False
#select O as random

while gamerunning:
    print_board(board)
    user_inp(board)
    horizontal(board)
    vertical(board)
    diagnol(board)
    check(board)
    switch()
    #computer(board)
    tie(board)
