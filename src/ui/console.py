class ConsoleUI:
    def __init__(self):
        """The ConsoleUI-class is responsible for the user interface of the program.
        The methods of the class that print text on the terminal will also return the 
        same text that they printed. This makes the testing of the class smoother.
        """
        pass

    def create_start_menu(self):
        header = "Fifteen Puzzle Solver"
        print(header)
        return header