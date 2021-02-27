# Master Mind
# Implemented GIT

import sys
import random

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

print("""
Welcome to Mastermind!
This game has been developed by Rhonda Jorgensen
For the course UO Programming Fundamentals SP1 2021

 """)

# Create our classes
class Game:
    pass
    # displayMenu
    def display_menu(self):
        print("Select which game you want to play?")
        print("(A) Original Mastermind for 2 players")
        print("(B) Original Mastermind for 1 player with Computer Support")
        print("(C) Mastermind 44 for 4 players")
        print("(D) Mastermind 44 for 4 players with computer support")
        print("(E) Exit")
        print()
        print("**********************************************************")
        print("Enter your choice [Press A, B, C, D, or E]\n")
    
        # Get the user's choice (THINK THIS MIGHT GO BEFORE ENTER YOUR CHOICE)
        choice = input(": ")

        # Validate the choice.
        
        while choice.lower not in [A, B, C, D, E]:
            choice = int(input('Enter a valid choice [Press A, B, C, D, or E]: '))

        # return the user's choice.
        return choice


class MasterMind:
    pass

class MasterMind44(MasterMind):
    pass

# This could be displayed in Game methods yet to decide
class Board:
    pass

class Players:
    def __init__(self, playerName, playerScore, playerRole):
        self.playerName = playerName         
        self._playerScore = None         
        self.playerRole = True         
        
    # Create the setters outline our constraints
    def set_playerName(self, playerName):
        self.playerName = playerName
        
    def set_playerScore(self, playerScore):
        if playerScore >= 0:
            self.__playerScore = playerScore
        else:
            raise Exception("Error: score can not be anything other than number")

    def set_playerRole(self):
        pass 
        # if choice is master mind 2 player 
        # then player role rotates between code maker and code breaker
        # else code maker is computer

        # if choice is master mind 44
        # then player is 1, 2, 3, or 4
        # and computer provides the hints and holds the clue created

class CodeMaker:
    def __init__(self):
        pass

    def computerCode(self):
        # Computer creates a random code
        code = []
        code_length = 4 
        peg_colours = ["Red", "Green", "Blue", "Cyan", "Magenta", "Yellow"] 
        for peg in range(0, code_length):
            code.append(random.choice(peg_colours))
        return code

class CodeBreaker:
    def __init__(self):
        pass

# This can be with Computer or CodeMaker
class RevealCode:
    pass

# This might be best inside CodeBreaker
class MakeGuess:
    def __init__(self, guess):
        self.guess = guess   
        self.__guessCount = None 

    # Create the setters with validation


    


        # we will need to set a counter to count how many guesses 
        # Easy = 12 guesses, Medium = 8 guesses, Hard = 6 Guesses

    pass

# This can be with Computer or CodeMaker
class Hint:
    pass






# Call to display
print(Game.display_menu)

#sys.exit()