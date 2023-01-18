import os

# Shows the position of each value on the board
print("Welcome to Tic-tac-toe!")
print("The positions of the board are: ")
print('7' + '|' + '8' + '|' + '9')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('1' + '|' + '2' + '|' + '3')
print("Enjoy your time playing!")
print (" ")

# Assigning value to the board
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

# Creating a empty list
board_keys = []

for key in theBoard:
    board_keys.append(key)

# Method that prints out the board each time with the updated values
def printBoard(board):
    print (" ")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print (" ")

# The main function which has all the gameplay functionality.
def main():

    turn = 'X'
    
    # Counts the amount of time both player have gone
    count = 0
    
    
    # Runs while COUNT is not equal to 9
    loop = True
    while loop:
        if (count==9):
            break
        printBoard(theBoard)
        # Records the number which the players want to place on the board
        move = input("It's your turn, " + turn + ". Move to which place: ")
        
        # Checks to make sure that the input provided by the user is a numeric value
        if move.isnumeric():  
            if (int(move) >= 1 and int(move) <= 9): # check if entered value is between 1 and 9
                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                    # This changes the turn of the players
                    if turn =='X':
                        turn = 'O'
                    else:
                        turn = 'X' 
                else:  # if place is already filled
                    print("That place is already filled. Please pick a new spot.")
                    continue 
            else:  # if entered number is less than 1 or greater than 9
                print("Please enter a number from 1-9.")
        else:   # if entered number is not a numeric vaue
            print("Please enter a numeric number between 1-9.")
        
            
        # Checks if any of the players X or O have won,for every move after 5 moves. 
        if count >= 5:
            # Checks the top line left to right
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            # Checks the middle line left to right
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            # Checks the bottom line left to right
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            # Checks down the left side
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            # Checks down the middle
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            # Checks down the right side
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break 
            # Checks the diagonal
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            # Checks the diagonal
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break 

        # If neither player wins and the board is full, the game is announced as tie
        if count == 9:
            print("\nGame Over.\n")                
            print("The game was a tie.")
       
    
    # This is to check if the user wants to play again
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "
        # This command clears the terminal
        os.system("cls")
        main()
    else:
        print("Have a great day!")

if __name__ == "__main__":
    main()