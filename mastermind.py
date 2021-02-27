# Master Mind
# Implemented GIT


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
        print("Enter your choice [Press A, B, C, D, or E]")


class MasterMind:
    pass

class MasterMind44:
    pass

# This could be displayed in Game methods yet to decide
class Board:
    pass

class Players:
    pass

class CodeMaker:
    pass

class CodeBreaker:
    pass

class RevealCode:
    pass

class MakeGuess:
    pass

class Hint:
    pass






# Call to display
Game.display_menu()