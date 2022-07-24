class ConsoleUI:
    def __init__(self, board):
        """The ConsoleUI-class is responsible for the user interface of the program.
        The methods of the class that print text on the terminal will also return the 
        same text that they printed. This makes the testing of the class smoother.
        """
        self.board = board

    def create_start_menu(self):
        header = "Fifteen Puzzle Solver"
        print(header)
        return header

    def print_board(self):
        tile_values = self.board.get_board()
        result = "+-----+\n"

        for i in range(4):
            for j in range(5):
                tile_value = tile_values[i][j]
                tile = f"|  {tile_value}   |\n+-----+"
                result += tile
        print(result)
        return result