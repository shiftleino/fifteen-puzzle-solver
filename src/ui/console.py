class ConsoleUI:
    """The ConsoleUI-class is responsible for the text-based user interface of 
    the program.
    """
    def __init__(self, board):
        self.board = board

    def create_start_menu(self):
        """Creates the start menu of the program and asks user's 
        choice for the heuristic.

        Returns:
            string: User's choice for the heuristic: "1" or "2".
        """
        print("Fifteen Puzzle Solver\n")
        choice = input("Choose which heuristic to use:\n1. Manhattan-distance\n2. Hamming-distance\n>>> ")
        return choice

    def create_end_menu(self):
        """Creates the end menu of the program and asks user's
        choice to continue or exit.

        Returns:
            string: User's choice to continue or exit: "s" or "q".
        """
        print("A solution to the puzzle was found, final result:\n")
        self.print_board()
        choice = input("To return to the start menu press s, to exit press q\n>>> ")
        return choice

    def print_board(self):
        """Outputs the current board to the console as a string.
        """
        tile_values = self.board.get_board()
        result = "\n" + 4*"+-----+" + "\n"
        for i in range(4):
            for j in range(4):
                tile_value = tile_values[i][j]
                if tile_value == 16:
                    tile_value = ""
                tile = f"|{tile_value:^5}|"
                result += tile
            result+= "\n" + 4*"+-----+" + "\n"
        print(result)
