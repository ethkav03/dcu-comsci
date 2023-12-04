class Board:
    """Represents the Go game board."""

    def __init__(self, size):
        """Initialize the board with the specified size."""
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def isLegalMove(self):
        """This function will check if the player has made a valid placement"""
        # checks theres a stone in intersection already
        # checks if move is a suicide move or not

    def placeStone(self, x, y, colour):
        """Place a stone of the specified color at the intersection."""
        self.grid[x][y] = colour
        # Update stone groups and liberties as needed

    def handleCaptures(self, player):
        """This function will handle the capturing of territory on the board"""
        # updates the currents players captures
        # remove the stone from the array and set it back to 0
        

    def checkAdjacent(self):
        """This function will recursively check all adjacent intersections to the placed stone"""
        # checks the status of each intersection north, south, east, west, and then recursively 
        # checks the north, south etc for each liberty

    def getSize(self):
        """Get the size of the Board group."""
        return self.size
    
    def getGrid(self):
        """Get the grid of the Board group."""
        return self.grid


class Group:
    """Represents a group of stones on the Go board."""

    def __init__(self, colour):
        """Initialize a stone group with a specified color."""
        self.colour = colour
        self.stones = []  # List of Stone objects that belong to the group
        self.liberites = []  # Define the liberties structure as needed

    def getColour(self):
        """Get the color of the stone group."""
        return self.colour

    def getLiberites(self):
        """Get the liberties of the stone group."""
        return self.liberites
    
    def getStones(self):
        """Get the stones of the stone group."""
        return self.stones

    def addStone(self, stone):
        """Add a stone to the group."""
        self.stones.append(stone)
        # Update the liberties of the group

    def addLiberties(self, liberty):
        """Adds coordinates of a liberty to list of liberties"""
        self.liberites.append(liberty)

    def popLiberties(self, liberty):
        """Removes coordinates of a liberty from list of liberties"""
        self.liberites.pop(liberty.index())


    def mergeGroups(self, group):
        """Merge this group with another group."""
        if self.colour == group.colour:
            self.stones.extend(group.stones)
            # Update the liberties of the merged group

from enum import Enum

class Stone(Enum):
    WHITE = 1
    BLACK = 2

class Player:
    """Represents a player in the Go game."""

    def __init__(self, name, color):
        """Initialize a player with a name and stone color."""
        self.name = name
        self.color = color
        self.score = 0
        self.captures = 0
        self.passTurn = False
        self.resign = False

    def getName(self):
        """Get the name of the player."""
        return self.name

    def getScore(self):
        """Get the player's current score."""
        return self.score

    def getCaptures(self):
        """Get the number of opponent stones captured by the player."""
        return self.captures

    def getColor(self):
        """Get the color of the player's stones."""
        return self.color
    
    def getResign(self):
        """Get the color of the player's stones."""
        return self.resign
    
    def getPass(self):
        """Get the color of the player's stones."""
        return self.passTurn
    
    def resignGame(self):
        """Sets resign to true."""
        self.resign = True
        return 
    
    def playerPass(self):
        """Sets pass to true."""
        self.passTurn = True

    def resetPass(self)
        """Set pass back to false"""
        self.passTurn = False

    def calcTerritory(self)
        """Activated at the end of the game"""
        lst = [] 
        # List will store tuples of array coordinants
        # Search algorithm to find empty intersections contained in groups
        # returns the length if the list
        return len(lst)
    
    def PlayerScore(self, teritory, captures, stones)
        """Calculates the players total score"""

        total = teritory + capture + stones
        
        return total 
    
    def trackPlayerCaptures(self, n)
        """Updates each time a stone is captured"""
        self.captures += n




class Game:
    """Represents a game of Go."""

    def __init__(self, size):
        """Initialize a new game with a board and two players."""
        self.board = Board(size)
        self.white_player = Player()
        self.black_player = Player()
        self.is_game_over = False
        self.current = Stone.BLACK # Black always starts

    def startNewGame(self, player1, player2):
        """Start a new game with the current players."""
        # Initialize the game state
        #creates a loop of commands to be ran for the game to function round by round
        while not self.is_game_over and (
            not player1.resign and not player2.resign) and (
                not player1.passTurn or not player2.passTurn):

        #end  loop
        endGame() 

    def endGame(self):
        """End the current game."""
        # Calculate and display the final score
        wTeritory = white_player.calcTeritory()
        # calculate all white stones in board
        wScore = white_player.playerScore()

        return 