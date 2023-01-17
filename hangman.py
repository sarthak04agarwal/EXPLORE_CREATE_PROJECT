import random


# Creates an empty list of the correctly guessed
correctly_guessed_letters = []

# Creates an empty list of the incorrectly guessed
incorrectly_guessed_letters = []

# Creates an empty variable of the that is supposed to be gussed
randomly_chosen_word = ""

# Creates a variable to keep track of the lives
lives_left = 6

# Variable to says if the game is over or not
game_over = False

# Method that chooses a random word that is to be gussed
def choose_random_word():
    global randomly_chosen_word

    acceptable_words = [
        "Computer",
        "Science",
        "Keyboard",
        "Mouse",
        "Monitor",
        "Python",
        "Java"
    ]

    randomly_chosen_word = random.choice(acceptable_words)
    randomly_chosen_word = randomly_chosen_word.lower()

# This method draws the word that is to be guessed
def draw_word():
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

#Will draw the hangman drawing based on the number of lives left
def draw_hangman():
    global lives_left

    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|")
        print("|           ")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|            ")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / ")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")

# Checks if the user types only 1 letter that has not been used before
def get_one_valid_letter():
    
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter guess letter: ")
        # Removes any spaces that are black to make sure that the letter that is to be guessed is only of length 1
        letter = letter.strip()
        # Turn all the character in the variable LETTER to lowercase
        letter = letter.lower()
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be of length 1")
        # The .isalpha() method checks if the string provided is between the alphabet a-z
        elif letter.isalpha():
            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                print("You have already guessed the letter " + letter + ", please try again")
            else:
                is_letter_valid = True
        else:
            print("Letter must be (a-z)")

    return letter

# Checks if the letter guessed is correct or wrong and will update variables
def guess_letter():
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global lives_left

    letter = get_one_valid_letter()
    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        lives_left -= 1

# Checks to see if the player has won or not
def check_for_game_over():
    global lives_left
    global game_over
    global correctly_guessed_letters
    global incorrectly_guessed_letters

    if lives_left <= 0:
        game_over = True
        draw_hangman()
        print("You lost, the word was " + randomly_chosen_word + ".")
        restartGame()
    else:
        guessed_all_letters = True
        for letter in randomly_chosen_word:
            if letter not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print("You won!")
            restartGame()
# Method that asks the user if they want to play again            
def restartGame():
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global randomly_chosen_word
    global lives_left
    global game_over
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        correctly_guessed_letters = []
        incorrectly_guessed_letters = []
        randomly_chosen_word = ""
        lives_left = 6
        game_over = False
        print(" ")
        main()
            
    
# The main method which calls every other method
def main():
    global game_over
    global randomly_chosen_word

    print("Welcome to Hangman!")
    status = input("1. Do you want to write your own word\n2. Word is picked randomly\nPlease pick either number 1 or number 2: ")
    if status == '1':
        randomly_chosen_word = input("\nPlease pick your word: ")
    elif status == '2':
        choose_random_word()
    else:
        print("Invalid option.")
        return 
        
    # While the game is not over this will keep print the Already letter that were guessed
    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print("Incorrect guesses: ")
            print(incorrectly_guessed_letters)

        guess_letter()
        check_for_game_over()


if __name__ == '__main__':
    main()