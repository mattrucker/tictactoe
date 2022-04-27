import curses

def main():
    board = init_board()
    #display_board()
    game()

def init_board():
    board = [position for position in range(9)]

def display_board():
    s = curses.initscr()
    w = curses.newwin(7, 7, 0, 0)
    w.box()
    w.vline(1, 2, "|", 5)
    w.vline(1, 4, "|", 5)
    w.hline(2, 1, "_", 5)
    w.hline(4, 1, "_", 5)
    #w.addstr(1, 1, "0")
    #w.addstr(1, 3, "1")
    #w.addstr(1, 5, "2")
    #w.addstr(3, 1, "3")
    #w.addstr(3, 3, "4")
    #w.addstr(3, 5, "5")
    #w.addstr(5, 1, "6")
    #w.addstr(5, 3, "7")
    #w.addstr(5, 5, "8")
    w.refresh()
    c = w.getch()
    if c == "q":
        curses.endwin()

def checkWinCondition():
    if board[0] == board[1] == board[2] or
    board[3]  ==  board[4] == board[5] or
    board[6] == board[7] == board[8] or
    board[0] == board[4] == board[8] or
    board[2] == board[4] == board[6] or
    board[0] == board[3] == board[6] or
    board[1] == board[4] == board[7] or
    board[2] == board[5] == board[8]
        return True
    elif
        return False

def game():
    winCondition = 0
    while winCondition == 0:
        x = input("Player X, select your next position:")
        if checkWinCondition()
            print("Congratulations player X on the W!")
        else:
        o = input("Player O, select your next position:")
        checkWinCondition()





main()