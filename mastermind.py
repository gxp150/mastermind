# Master Mind
# Implemented GIT

import sys
import os
import random

# Create our skeleton using our UML


class Game:
    """
    The Game Class

    We create the Game class so that we can display
    the menu for the user to choose from.
   """
    # pass
    # displayMenu

    def display_menu(self):
        print("*********************************************************")
        print("Select which game you want to play?")
        print("(A) Original Mastermind for 2 players")
        print("(B) Original Mastermind for 1 player with Computer Support")
        print("(C) Mastermind44 for 4 players")
        print("(D) Mastermind44 for 4 players with Computer Support")
        print("(E) Exit\n")
        print("*********************************************************")

        choice = ''

        # Validate the choice.
        while choice.lower() not in ["a", "b", "c", "d", "e"]:
            # Get the user's choice (THINK THIS MIGHT GO BEFORE ENTER YOUR CHOICE)
            choice = input("*Enter your choice [Press A, B, C, D, or E]*\n")

        return choice

# Create SuperClassMasterMind the games will draw from
# List your common elements here


class MasterMind():
    """
    The MasterMind Class

    This class will be our Parent Class
    that the other variations of MasterMind will
    inherit from.
    """
    # codemaker = random.choice([player1, player2])
    # if codemaker = player1:
    # then codebreaker = player2
    # else codebreaker = player1

    pass


class CodeMaker:
    def __init__(self):
        pass

    # Computer creates a random code
    def computerCode(self, code_length):
        """
        Generate the random code for the Computer

        Parameters:
        code_length: Restrict code to 4

        Returns:
        code: Random generated code for the Codebreaker to Crack
        """

        code = []

        peg_colours = {"R": "Red", "B": "Blue", "G": "Green",
                       "Y": "Yellow", "M": "Magenta", "C": "Cyan"}

        for peg in range(code_length):
            code.append(random.choice(list(peg_colours.keys())))
        # Testing code
        print(code)
        return code

    class MakeGuess:
        def __init__(self, guess):
            self.guess = guess
            self.__guessCount = None

            validate_code(code, length)

    # Create the setters with validation
    # we will need to set a counter to count how many guesses
    # Easy = 12 guesses, Medium = 8 guesses, Hard = 6 Guesses

    pass

# This can be with Computer or CodeMaker


def validate_code(code, length):
    valid_code = True

    peg_colours = {"R": "Red", "B": "Blue", "G": "Green",
                   "Y": "Yellow", "M": "Magenta", "C": "Cyan"}

    if len(code) != length:
        valid_code = False

    for n in range(len(code)):
        if code[n].upper() not in list(peg_colours.keys()):
            valid_code = False

    if valid_code == False:
        print("Please enter a valid code.")

    return valid_code


class MasterMindComputer():
    # Create the MasterMind Computer Version - Option B
    # List all the instructions and build out
    # Replicate and modify for the other parts
    def __init__(self, player1):
        self.player = player1
        print("Welcome ", player1)
        print("You are the codebreaker for this game.")
        print("You need to break the Code that consists of four pegs.")
        print("Each peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
        print("Break the Code by specifying four characters where each character indicates a colour as above.")
        print("For example, BYRG represents the code Blue Yellow Red Green.")
        print("Feedback will be provided on your attempted Code.")
        print("Black peg means there is a peg in your Code with correct colour and correct order.")
        print("White peg means there is a peg in your Code with correct colour but incorrect order.")
        print("You will get 12 attempts to break the code.")
        print("Good luck!")

    def play(self, player1):
        maker = CodeMaker()
        breaker = CodeBreaker()

        code = maker.computerCode(4)

        max_attempts = 12
        attempts = 0

        guess = []

        peg_colours = {"R": "Red", "B": "Blue", "G": "Green",
                       "Y": "Yellow", "M": "Magenta", "C": "Cyan"}

        for attempts in range(max_attempts):
            black = 0
            white = 0

            guess = breaker.getGuess(player1, 4)

            print("Attempt #", attempts + 1, ":")

            for n in range(len(guess)):
                print(peg_colours[guess[n]].upper())

            for n in range(len(code)):
                if guess[n] == code[n]:
                    black = black + 1
                elif guess[n] in code:
                    white = white + 1
                # else:
                    # raise TypeError("Please enter a peg colour from the range supplied")
                    # Minimum 4 - 3 breaks the game currently as does a digit

            print("Feedback #", attempts + 1, ":")

            for n in range(black):
                print("BLACK")

            for n in range(white):
                print("WHITE")

            if guess == ''.join(code):
                break

        if guess == ''.join(code):
            print("Congratulations ", player1,
                  "! You have broken the Code in ", attempts + 1, " attempts.")
        else:
            print("Better luck next time, [", player1, "] , Computer WINS!")


class MasterMind44(MasterMind):
    """
    MasterMind 44

    Each player is assigned a position to allocate a colour to
    There will be 5 positions
    So I guess one can be blank or assigned by the computer
    Then each player has a guess, they will know the position of their own pin colour
    The computer will respond having gathered all the pins retrieved by each player
    And show the results same as MasterMind
    The first player to get it is the winner
    """
    # start here

    def __init__(self):
        # Will need to ask for the 4 player names
        print("Welcome to MasterMind44!")
        print("The computer will create the secret code and reveal")
        print("four pegs of the five positions one-by-one individually to each player.")
        print("During revealing each position, only the requested player should look at the screen")
        print("Each peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
        print("[", player1, "] When you are read for one position of the code to be revealed on the screen press <enter>")
        # create version of game here

    pass


# This could be displayed in Game methods yet to decide
class Board:
    pass


class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.__playerScore = 0
        # self.playerRole = True

    # Create the setters outline our constraints
    def set_playerName(self, playerName):
        self.playerName = playerName

    def set_playerScore(self, playerScore):
        if playerScore >= 0:
            self.__playerScore = playerScore
        else:
            raise Exception(
                "Error: score can not be anything other than number")

    def set_playerRole(self):
        pass
        # if choice is master mind 2 player
        # then player role rotates between code maker and code breaker
        # else code maker is computer

        # if choice is master mind 44
        # then player is 1, 2, 3, or 4
        # and computer provides the hints and holds the clue created


class CodeBreaker:
    def __init__(self):
        pass

    def getGuess(self, player1, length):
        # need to validate this is a valid guess

        valid_code = False

        while valid_code == False:
            valid_code = True

            print("[", player1, "] Enter the Code to break:")
            guess = input()

            valid_code = validate_code(guess, length)

        """        
        try:
            print("[", player1, "] Enter the Code to break:")
            guess = input()
        except (KeyError, ValueError, TypeError):
            print("You need to enter a colour from the available list")
            print(
                "Each peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
            guess = input()
"""
        return guess.upper()


class RevealCode:
    pass

# This can be with Computer or CodeMaker


class Hint:
    pass


def main():
    # welcome banner
    print("Welcome to MasterMind!")
    print("This game has been developed by Rhonda Jorgensen")
    print("For the course UO Programming Fundamentals SP1 2021\n")

    # display menu
    game = Game()
    choice = game.display_menu()

    if choice.lower() == "a":
        print("Sorry this game is not available, try another option\n")
        choice = game.display_menu()
        # player1 = input("Player 1: What is your name? ")
        # player2 = input("Player 2: What is your name? ")

    elif choice.lower() == "b":
        player1 = input("Player 1: What is your name? ")

        mmgame = MasterMindComputer(player1)
        mmgame.play(player1)

    elif choice.lower() == "c":
        print("Sorry this game is not available, try another option\n")
        choice = game.display_menu()

    elif choice.lower() == "d":
        print("Sorry this game is not available, try another option\n")
        choice = game.display_menu()
        # player1 = input("Player 1: What is your name? ")
        # player2 = input("Player 2: What is your name? ")
        # player3 = input("Player 3: What is your name? ")
        # player4 = input("Player 4: What is your name? ")

    elif choice.lower() == "e":
        print("Goodbye")


if __name__ == '__main__':
    main()

    sys.exit()
