class ConsoleUI:
    """The ConsoleUI-class is responsible for the text-based user interface of 
    the program.
    """

    def print_start_menu(self):
        """Creates the start menu of the program and asks user's 
        choice for the heuristic.

        Returns:
            string: User's choice for the heuristic: "1" or "2".
        """
        print("Fifteen Puzzle Solver\n")
        choice = input("Choose which heuristic to use:\n1. Manhattan-distance\n2. Hamming-distance\n3. Improved Manhattan-distance\n>>> ")
        return choice

    def print_end_menu(self):
        """Creates the end menu of the program and asks user's
        choice to continue or exit.

        Returns:
            string: User's choice to continue or exit: "s" or "q".
        """
        choice = input("\nTo return to the start menu press s, to exit press q\n>>> ")
        return choice

    def print_start_position(self, tile_values):
        """Shows the starting position of the board in the console.

        Args:
            tile_values ([][]int): Starting values of the board.
        """
        print("\nSolving the following starting placement:")
        self.print_board(tile_values)

    def print_solution_steps(self, solution_steps, duration):
        """Shows the optimal steps that the solver took to solve the puzzle.

        Args:
            solution_steps (_type_): _description_
            duration (_type_): _description_
        """
        print(f"\nA solution to the puzzle was found in {duration:.2f} seconds, the optimal steps are:\n")
        for board in solution_steps:
            self.print_board(board)

    def print_board(self, tile_values):
        """Outputs the current board to the console as a string.
        """
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
