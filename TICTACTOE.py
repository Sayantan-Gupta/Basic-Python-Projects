#TIC TAC TOE GAME
from IPython.display import clear_output
import random

#Display the Game Board
def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


#Take in a player input and assign their marker as 'X' or 'O'

def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: DO you want to play as 'X' or as 'O'").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
        

#Function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, postion):
    board[postion] = marker

#Function to check if someone has won, takes marker as input

def win_check(board, m):
    return (
        (board[1] == m and board[2] == m and board[3] == m) or
        (board[4] == m and board[5] == m and board[6] == m) or
        (board[7] == m and board[8] == m and board[9] == m) or
        (board[1] == m and board[5] == m and board[9] == m) or
        (board[7] == m and board[5] == m and board[3] == m) or
        (board[7] == m and board[4] == m and board[1] == m) or
        (board[8] == m and board[5] == m and board[2] == m) or
        (board[9] == m and board[6] == m and board[3] == m)
    
    )
    
    
#Function to randomly decide which player plays first turn initially

def first_turn():
    if random.randint(0,2) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
        
        
#Function that returns a boolean indicating whether a space on the board is freely available on given input postion

def space_check(board, position):
    return board[position] == ' '
    
    
#Function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def board_full_check(board):
# Range index started from 1 because board[0] will always be empty
    for i in range(1, 10):
        if space_check(board, i):
            return False
            
    return True
    
#Function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please enter you chosen Position(1-9) : "))
        
    return position
    
#Function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    return input("Do you want to play again? Please enter Yes or No: ").lower().startswith('y')
    
    
#Building the Game

print("Welcome to Tic Tac Toe Game")

while True:
    game_board = [' ']*10
    player1_mark, player2_mark = player_input()
    print(player1_mark)
    print(player2_mark)
    turn = first_turn()
    
    print(f"{turn} will play first please")
    
    play_game = input("Are you both ready to play? Yes or No: ")
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
        
    while game_on:
        
        if turn == 'Player 1':
            display_board(game_board)
            
            position = player_choice(game_board)
        
            place_marker(game_board, player1_mark, position)
        
            if win_check(game_board, player1_mark):
                display_board(game_board)
                print("Hurray!! Player 1 has won the game")
                game_on = False
            
            else:
                if board_full_check(game_board):
                    display_board(game_board)
                    print("The Game is drawn")
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
            
            display_board(game_board)
            
            position = player_choice(game_board)
        
            place_marker(game_board, player2_mark, position)
        
            if win_check(game_board, player2_mark):
                display_board(game_board)
                print("Hurray!! Player 2 has won the game")
                game_on = False
            
            else:
                if board_full_check(game_board):
                    display_board(game_board)
                    print("The Game is drawn")
                    game_on = False
                else:
                    turn = 'Player 1'
                    
                    
if not replay():
    print("Thank you for playing the game, Code developed by Sayantan Gupta")
    break
