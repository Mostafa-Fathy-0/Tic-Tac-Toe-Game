# Tic_Tac_Toe_Game
# Coded By Mostafa Fathy

# Game Board
board = [[' ',' ',' '], # 0,0  0,1  0,2
         [' ',' ',' '], # 1,0  1,1  1,2
         [' ',' ',' ']] # 2,0  2,1  2,2
# Game Controlers
win = 1
draw = -1
running = 0
stop = 1
mark = 'X'

# Get player names
# This function will take names from users
def get_player_names():
    player1 = input('Please enter First Player name: ')
    while not player1:
        player1 = input('Invalid input. Please enter First Player name: ')
    player2 = input('Please enter Second Player name: ')
    while not player2:
        player2 = input('Invalid input. Please enter Second Player name: ')
    return player1, player2

# Show_Board
# This function will show the board on screen
def show_board():    
    print(" %c | %c | %c " % ((board[0][0]),(board[0][1]),(board[0][2])))    
    print("___|___|___")    
    print(" %c | %c | %c" % ((board[1][0]),(board[1][1]),(board[1][2])))    
    print("___|___|___")    
    print(" %c | %c | %c " % ((board[2][0]),(board[2][1]),(board[2][2])))    
    print("   |   |   ") 

# Check_Place
# This function will check whether a place on the board is empty or not
def check_place_in_board(x):
    if board[x//3][x%3] == ' ':
        return True 
    else:
        return False

# Check_Win
# This function will check if player wins, draws or loses
def check_win():
    # to win, you must fill 3 places in the board with your symbol in a vertical, horizontal or diagonal line
    # Horizontal winnig lines ---> 1-2-3 , 4-5-6 , 7-8-9
    # Vertical winning lines---> 1-4-7 , 2-5-8 , 3-6-9 
    # Diagnol winning lines ---> 1-5-9 , 3-5-7 
    # Horizontal Win ! 
    # Board Line ----> 1 2 3
    if ((board[0][0]) == (board[0][1]) and (board[0][1]) == (board[0][2]) and (board[0][0]) != ' ') :
        return True
    # Board Line ----> 4 5 6    
    elif ((board[1][0]) == (board[1][1]) and (board[1][1])== (board[1][2]) and (board[1][0]) != ' ') :
        return True
    # Board Line ----> 7 8 9    
    elif ((board[2][0]) == (board[2][1]) and (board[2][1])== (board[2][2]) and (board[2][0]) != ' ') :
        return True    
    # Vertical Win !
    # Board Line ----> 1 4 7
    elif (board[0][0] == board[1][0] and board[1][0]== board[2][0] and board[0][0] != ' ') :
        return True
    # Board Line ----> 2 5 8    
    elif (board[0][1] == board[1][1] and board[1][1]== board[2][1] and board[0][1] != ' ') :
        return True
    # Board Line ----> 3 6 9    
    elif (board[0][2] == board[1][2] and board[1][2]== board[2][2] and board[0][2] != ' ') :
        return True 
    # Diagonal Win !
    # Board Line ----> 1 5 9
    elif (board[0][0] == board[1][1] and board[1][1]== board[2][2] and board[0][2] != ' ') :
        return True
    # Board Line ----> 3 5 7    
    elif (board[0][2] == board[1][1] and board[1][1]== board[2][0] and board[0][2] != ' ') :
        return True
    # Draw
    elif ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return draw
    else :
        return running 

# Play_Game
# This function will run the game and handle the player inputs
def play_game(player1, player2):
    player = 1
    game = running
    while (game == running) :
        show_board()
        if (player % 2 != 0) :
            print("{}'s turn".format(player1))
            mark = 'X'
        else :
            print("{}'s turn".format(player2))
            mark = 'O'
        choice = input("Choose a number between 1-9 where you want to mark: ")
        try:
            choice = int(choice)
            if 1 <= choice <= 9:
                if check_place_in_board(choice-1):    
                    board[(choice-1)//3][(choice-1)%3] = mark    
                    player += 1    
                    game = check_win()
                else:
                    print("This place is already marked. Choose another place.")
            else:
                print("Invalid input. Choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Choose a number between 1 and 9.")
    show_board()    
    if game == draw:    
        print("Game Draw")    
    elif game == win:    
        player -= 1    
        if player % 2 != 0:    
            print("Awesome {} ,You're the winner ^_^".format(player1))
        else:    
            print("Awesome {} ,You're the winner ^_^".format(player2))

# Main function
def main():
    print("Tic-Tac-Toe game played on a 3x3 board\ntwo players take turns marking X's and O's until one player gets 3 in a row or the board filled without a winner.\nAre you ready to test your skills ?\nLet's get started!\n")
    player1, player2 = get_player_names()
    play_game(player1, player2)
        
if __name__ == '__main__':
    main()

 

