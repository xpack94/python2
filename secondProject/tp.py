import sys
import os


class bcolors:
    ''' Declare the different colors using ANSI '''
    B = '\033[94m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    ENDC = '\033[0m'


class GameBoard:
    '''Initialize, print and manage the game board.

    Public methods :
        update()
    '''

    def __init__(self):
        '''Constructor of GameBoard class.

        Apply the configuration and rules.
        Set the dimension of the board and create it's Cell objects.
        Apply the initial state and create arrays of pointers.
        '''
        self._config = self._parseConfig()
        self._rules = self._parseRules()
        self._width = self._config["width"]
        self._height = self._config["height"]
        self._board = [[Cell(False) for x in range(self._width)] for y in range(self._height)]
        self._setInitialState()
        self._setCellsSurroundingPointers()

    def __str__(self):
        '''ToString function of GameBoard class.

        Returns :
                Str: Formatted Board in String ready to be printed out.
        '''
        output = ''
        for idx in range(len(self._board)):
            for cell in self._board[idx]:
                output += ' {}'.format(cell)
            output += '\n'

        return output

    def update(self):
        ''' Update the board for one iteration

        Each cell is updated individually based on his status and the rule apply to it.
        '''
        self._setCellsSurrounding()

        for idx in range(len(self._board)):
            for cell in self._board[idx]:
                for rule in self._rules:
                    if cell.getStatus():
                        if cell.getOrganism()._color == rule.color:
                            if cell.lastSurrounding < rule.live or cell.lastSurrounding > rule.die:
                                cell.empty()
                                break
                    else:
                        if rule.born == cell.lastSurrounding:
                            cell.fill(Organism(rule.color))
                            break

    def _setCellsSurrounding(self):
        ''' For every cell in the board, call setSurrounding().'''
        for idx in range(len(self._board)):
            for cell in self._board[idx]:
                cell.setSurrounding()

    def _setInitialState(self):
        ''' Assign initial cells on the board from the config file. '''
        for etat in self._config["etats"]:
            self._board[etat["x"]][etat["y"]].fill(Organism(etat["couleur"]))

    def _setCellsSurroundingPointers(self):
        ''' Assign pointers to squares around cells

        For every Cell object, add an array of pointers pointing to all the 8 surrounding cells.
        If the cell is on either side of the board, pass the positions outside of the board.

        Raises:
            IndexError: Prevents from adding cells out of the board's bounds.
        '''
        for idx_line in range(len(self._board)):
            for idx_row, cell in enumerate(self._board[idx_line]):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            shift_line = idx_line + i
                            shift_row = idx_row + j
                            if shift_line < 0 or shift_row < 0 or (i == 0 and j == 0):
                                raise IndexError
                            cell.surroundingPointers.append(self._board[shift_line][shift_row])
                        except IndexError:
                            pass

    def _parseConfig(self):
        ''' Generate a dictionnary with the configurations (dimension, initial board) from config.txt

        We take in consideration that the config file is respecting the correct syntax format.
        We are not raising the two exeptions but we are exiting if they happen.

        Exceptions:
            IOError: Error while attempting to open the file.
            ValueError: Error with one of the value taken from the file.

        Returns :
                Dic: Contains the dimension of the board as well as every cell initially alive.
        '''
        config = {}
        config['etats'] = []
        try:
            with open('config.txt', 'r') as config_file:
                size = config_file.readline().rstrip('\n').split(",")
                config['width'] = int(size[0])
                config['height'] = int(size[1])

                for line in config_file:
                    if not line in '\n':
                        etat = line.rstrip('\n').split(",")
                        data = {'couleur': etat[0], 'x': int(etat[1]), 'y': int(etat[2])}
                        config['etats'].append(data)

        except IOError:
            print("The file cannot be opened")
            exit()

        except ValueError:
            print("Wrong syntax in the config file")
            exit()

        return config

    def _parseRules(self):
        ''' Generate a dictionnary with the configurations (dimension, initial board) from config.txt

        We take in consideration that the config file is respecting the correct syntax format.
        We are not raising the exception but we are exiting if it happen.

        Exception:
            IOError: Error while attempting to open the file.

        Returns :
                Dic: Contains the dimension of the board as well as every cell initially alive.
        '''
        rules = []
        try:
            with open('rules.txt', 'r') as rules_file:
                for line in rules_file:
                    data = line.rstrip('\n').split(":")
                    rule = data[1].split(",")
                    new_rule = Rule(data[0], int(rule[0]), int(rule[1]), int(rule[2]))
                    # this ensure we have the proper order R >> G >> B
                    if new_rule.color == 'R':
                        rules.insert(0, new_rule)
                    elif new_rule.color == 'G':
                        rules.insert(1, new_rule)
                    elif new_rule.color == 'B':
                        rules.insert(2, new_rule)
                    else:
                        rules.append(new_rule)

        except IOError:
            print("The file cannot be opened")
        return rules


class Organism:
    def __init__(self, color):
        '''Constructor of class Organism

        Args :
            color (Str): The color of the Organism.
        '''
        self._color = color

    def __str__(self):
        '''Print function of Organism

        If the color mode is activated, sets the different String values using the class bcolors.

        Returns :
                Str: The color of the organism.
        '''

        if arg == '-couleur' or arg == 'couleur':
            color = bcolors.B if self._color == 'B' else bcolors.R if self._color == 'R' else bcolors.G if self._color == 'G' else bcolors.Y
            return '{color}#{end}'.format(color=color, end=bcolors.ENDC)

        return self._color


class Cell:
    ''' A living of dead object representing a unit on the board.

    Public methods :
        empty()
        fill()
        getOrganism()
        getStatus()
        setSurrounding()
        getSurroundingCount()
    '''

    def __init__(self, status):
        ''' Constructor of Cell class.

        Assign the living state to the Cell object (status) as well as it's organism.
        Set it's number of neighbors to 0 and initialize the arrays pointing to the surrounding squares.

        Args :
            status (bool): True if the cell is alive, False otherwise.
        '''
        self._status = status
        self._organism = None
        self.surroundingPointers = []
        self.lastSurrounding = 0

    def __str__(self):
        ''' Print function of Cell

        Returns :
            Str: Formatted as followed : . for a non-existing cell and the organism's color for a living cell.
        '''
        if self._organism == None:
            return '.'
        return str(self._organism)

    def empty(self):
        ''' Kills a cell by putting it's status to none and removing the organism corresponding.'''
        self._status = False
        self._organism = None

    def fill(self, organism):
        ''' Put a cell to life by assigning it a status and an organism.

        Args :
            organism (Organism): Object with the color of the cell.
        '''
        self._status = True
        self._organism = organism

    def getOrganism(self):
        ''' Getter of the Organism object assigned to a cell. '''
        return self._organism

    def getStatus(self):
        ''' Getter of the status of the cell (True for filled, False for empty) '''
        return self._status

    def setSurrounding(self):
        ''' Calculate the number of cells around one cell at the present generation '''
        self.lastSurrounding = self.getSurroundingCount()

    def getSurroundingCount(self):
        ''' Return the number of Organism around himself (of all color) '''
        count = 0
        for cell in self.surroundingPointers:
            if cell.getStatus():
                count += 1

        return count


class Rule():
    '''Contain the specificities of each game rule.'''

    def __init__(self, color, born, live, die):
        ''' Constructor of Rule class.

        Assign the color of the cell on which the rules applies with the values corresponding.

        Args :
            color (Str): True if the cell is alive, False otherwise.
            born (int): The amount of cell needed for a new one to be borned.
            live (int): The minimal amount of cells needed for a specific cell to survive.
            die (int): The maximul amount of cells before a specific cell dies.
        '''
        self.color = color
        self.born = born
        self.live = live
        self.die = die

    def __str__(self):
        ''' ToString function of the class Rule.'''
        return '{}:{},{},{}'.format(self.color, self.born, self.live, self.die)


def cls():
    ''' Clean the screen by erasing previous text.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def animation(mainBoard):
    ''' Allow user to input "enter" for next generation or "exit" to quit '''
    while (True):
        nextUpdate = input("[exit] : ")
        if nextUpdate.lower() == 'exit' or nextUpdate.lower() == 'q':
            break
        cls()
        mainBoard.update()
        print(mainBoard)


def main():
    ''' Main function

    Loop and manage the user inputs for differents modes.
    Clear and refresh the board.

    Attributes :
            arg (Str): Input of the user regarding which action he wants to perform.

    Raises:
        IndexError: Prevents when no input.
    '''
    global arg
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = 'undefined'

    # looping until getting a correct argument
    while (True):
        # creating the main board
        mainBoard = GameBoard()

        cls()

        # all the possible modes and how the board will be updated
        if arg.isdigit() and int(arg) >= 0:
            # print the board ONCE after arg iteration
            for nb in range(int(arg)):
                mainBoard.update()
            # Print only after the nb of update necessary
            print(mainBoard)

        elif arg == "-animation" or arg == "animation":
            # print the initial board and then print a new board for each iteration
            print(mainBoard)
            animation(mainBoard)

        elif arg == "-couleur" or arg == "couleur":
            # print the initial board and then print a new board for each iteration with color
            print(mainBoard)
            animation(mainBoard)

        elif arg == "-exit" or arg == "exit":
            exit()

        arg = input('[<valeur>] [animation] [couleur] [exit] : ')


if __name__ == "__main__":
    main()

# -------------- RAPPORT DE CORRECTION ------------------------------------------
"""
Vous passez tous les tests, bravo! Votre code est clair et votre interface est
intéressante, c'est bien qu'on puisse revenir en arrière. Par contre cela fait
en sorte que vous ne respectez pas tout à fait le format de sortie. Vous auriez
pu l'ajouter en surplus avec un autre argument à passer!

Note: 107/100
	Tests: 60/60
	Respect du format de sortie: 7/10
	Qualité du code: 30/30
	Bonus1: +5
	Bonus2: +5

"""