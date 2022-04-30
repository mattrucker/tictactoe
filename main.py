def main():
    board = init_board()
    display_board(board)
    game(board)

def init_board():
    board = []
    for position in range(9):
        board.append(position + 1)
    return board

def display_board(board):
    #yay for fstrings
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print ("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print ("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def checkWinCondition(board):
    if board[0] == board[1] == board[2] or board[3]  ==  board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        return True
    else:
        return False

def game(board):
    winCondition = 0
    while winCondition == 0:
        x(board)
        display_board(board)
        if checkWinCondition(board):
            print("Good game. Thanks for playing! X wins!")
        else:
            o(board)
            display_board(board)
            if checkWinCondition(board):
                print("Good game. Thanks for playing! O wins!")
            else:
                continue
        for position in board:
            if board[position] != "x" and board[position] != "o" and checkWinCondition(board) == False:
                print("Tie!")
            

def x(board):
    x = input("x's turn to choose a square (1-9):")
    x = int(x)
    board.pop(x - 1)
    board.insert(x - 1, "x")
    return board

def o(board):
    o = input("o's turn to choose a square (1-9):")
    o = int(o)
    board.pop(o - 1)
    board.insert(o - 1, "o")
    return board

main()