from BinaryTree import BinaryTree
"""
    Author: Ethan Jordan
    Date: 11/01/2023
    Class: Advanced Python
    The main.py code is a Python program that implements a movie guessing game using a binary tree data
    structure.
    """

def loadGameFile(filePath):
    """
    Load a game file, extract the welcome message, help information, and construct a binary tree for the game.

    :param filePath: The path to the game file to load.
    :return: A tuple containing the game tree, help information, and welcome message.
    """
    gameTreeTemp = BinaryTree()
    helpInformation = None
    welcomeMessage = None

    # Open the game file
    with open(filePath, "r") as gameFile:
        # Iterate over each line in the file
        for line in gameFile:
            # Check if the line is a welcome message
            if isWelcomeMessage(line):
                welcomeMessage = line
            # Check if the line is help information
            elif isHelpInformation(line):
                helpInformation = line
            # If not, add the line to the game tree
            else:
                gameTreeTemp.insert(line)
    return gameTreeTemp, helpInformation, welcomeMessage

def isWelcomeMessage(line):
    """
    Check if a line is a welcome message.

    :param line: The line to check.
    :return: True if the line is a welcome message, False otherwise.
    """
    return not line[0].isdigit() and "Welcome" in line

def isHelpInformation(line):
    """
    Check if a line is help information.

    :param line: The line to check.
    :return: True if the line is help information, False otherwise.
    """
    return "- =" in line

def playGame(gameTreeTemp, welcomeMessage):
    """
    Play the game.

    :param gameTreeTemp: The game tree.
    :param welcomeMessage: The welcome message.
    """
    print(welcomeMessage)
    current = gameTreeTemp.getRoot()
    # Loop until reaching a leaf node
    while True:
        print(current.element[4:])
        if(current.left is None and current.right is None):
            break
        # Get the next node based on user input
        current = getNextNode(current)

def getNextNode(current):
    """
    Get the next node based on user input.

    :param current: The current node.
    :return: The next node.
    """
    notValidAnswer = True
    # Loop until receiving valid user input
    while(notValidAnswer):
        userInput = input("Answer: ")
        if(userInput.lower() == "y"):
            notValidAnswer = False
            current = current.right
        elif(userInput.lower() == "n"):
            notValidAnswer = False
            current = current.left
        else:
            print("Invalid Answer")
    return current

def loadNewGame(gamePath):
    """
    Load a new game.

    :param gamePath: The path to the current game file.
    :return: A tuple containing the new game path, game tree, help information, and welcome message.
    """
    newGamePath = input("Enter the path of your game: ")
    if newGamePath != gamePath:
        gamePath = newGamePath
        gameTreeTemp, helpInformation, welcomeMessage = loadGameFile(gamePath)
    return gamePath, gameTreeTemp, helpInformation, welcomeMessage

if __name__ == "__main__":
    gamePath = 'C:/Users/ejor5/OneDrive/Desktop/Code/MAINFRAME/GuessingGame/game1.txt'
    gameTreeTemp, helpInformation, welcomeMessage = loadGameFile(gamePath)

    # Main game loop
    while(True):
        firstInput = input("""
        * + Movie Guessing Game + *\n
        P - Play the game\n
        L - Load another game file\n
        D - Display the binary tree\n
        H - Help informationp\n
        X - Exit the program\n
        Enter your choice: 
        """)
        # Handle user input
        if firstInput.lower() == "p":
            # Play the game!
            playGame(gameTreeTemp, welcomeMessage)
        elif firstInput.lower() == "l":
            # Creates a new game through loadNewGame function, and re-assigns variables
            gamePath, gameTreeTemp, helpInformation, welcomeMessage = loadNewGame(gamePath)
        elif firstInput.lower() == "d":
            # Leads to the next menu that asks what type of display order
            gameTreeTemp.display()
        elif firstInput.lower() == "h":
            # Just prints the variable made in the first method
            print(helpInformation)
        elif firstInput.lower() == "x":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
