# Master Mind
# Implemented GIT

import sys
import os
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

# Create our classes
class Game:
    # pass
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
        print("Enter your choice [Press A, B, C, D, or E]: \n")
    
        # Get the user's choice (THINK THIS MIGHT GO BEFORE ENTER YOUR CHOICE)
        choice = input(": ")
        

        # Validate the choice.
        if choice.lower() == "a":
            player1 = input("Player 1: What is your name: ")
            player2 = print(input("Player 2: What is your name: "))
        
        elif choice.lower() == "b":
            player1 = input("Player 1: What is your name: ")
            
            mmgame = MasterMindComputer(player1)
            mmgame.play()
            
            # list my instructions here for this version of the game
            # implement each step



        elif choice.lower() == "c":
            print("Sorry this game is not available, try another option")
            return choice

        elif choice.lower() == "d":
            player1 = print(input("Player 1: What is your name: "))
            player2 = print(input("Player 2: What is your name: "))
            player3 = print(input("Player 1: What is your name: "))
            player4 = print(input("Player 2: What is your name: "))

        elif choice.lower() == "e":
            print("Goodbye")
            sys.exit()
        
        # Capture any other options entered
        # Possibly enter validation errors for integers here so programme doesnt crash
        else:
            print("You must enter a choice from A to E only")
            return choice

# Create SuperClassMasterMind the games will draw from
# List your common elements here



class MasterMind():
    pass

class MasterMindComputer():
    # start here
    def __init__(self, player1):
        self.player = player1
        print("Welcome ", player1, "\nYou are the codebreaker for this game")
        print("You need to break the Code that consists of four pegs.")
        print("Each peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
        print("Break the Code by specifying four characters where each character indicates a colour as above")
        print("For example, BYRG represents the code Blue Yellow Red Green")
        print("Feeback will be provided on your attemped Code")
        print("Black peg means there is a peg in your Code with correct colour and correct order.")
        print("White peg means there is a peg in your code with correct colour but incorrect order")
        print("You will get 12 attempts to break the code")
        print("Good Luck!")
        # create version of game here
        
    def play(self):
        # Now code the game
        # list all the instructions and build out
        # replicate and modify for the other parts
        pass


class MasterMind44(MasterMind):
    pass

# This could be displayed in Game methods yet to decide
class Board:
    pass

class Player:
    def __init__(self, playerName):
        self.playerName = playerName         
        self._playerScore = 0         
        #self.playerRole = True         
        
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


def main():
    print("Welcome to " + os.path.basename(__file__))
    print("This game has been developed by Rhonda Jorgensen")
    print("For the course UO Programming Fundamentals SP1 2021\n")
    
    # Call to display
    game = Game()
    choice = game.display_menu()

    #print("woo got through the menu!")

if __name__ == '__main__':
    main()

    #sys.exit()
