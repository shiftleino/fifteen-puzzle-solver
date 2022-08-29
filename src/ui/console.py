class ConsoleUI:
    """The ConsoleUI-class is responsible for the text-based user interface of 
    the program.
    """

    def run_game(self, game, gui):
        """Launches the game and runs it until user stops the program.

        Args:
            game (Game): The game object of the program.
            gui (GraphicalUI): The graphical user interface object of the program.
        """
        restart_choice = "s"

        while restart_choice == "s":
            heuristic, mode = self.print_start_menu()
            game.heuristic = heuristic
            if mode == "1":
                game.start_game_easy()
            else:
                game.start_game_hard()

            print("\nSolving the following starting placement:")
            self.print_board(game.tile_values)
            solution_steps, duration = game.solve_puzzle()
            print(f"\nA solution to the puzzle was found in {duration:.5f} seconds, showing the optimal steps (press space to show next)...\n")
            gui.show_solution(solution_steps)
            restart_choice = self.print_end_menu()

    def print_start_menu(self):
        """Creates the start menu of the program and asks user's 
        choice for the heuristic and the game mode (easy or hard).

        Returns:
            string: User's choice for the heuristic: "1", "2", or "3".
            string: User's choice for the mode: "1" or "2".
        """
        print("Fifteen Puzzle Solver\n")

        heuristic = input("Choose which heuristic to use:\n1. Manhattan-distance\n2. Hamming-distance\n3. Improved Manhattan-distance\n>>> ")
        while heuristic not in ("1", "2", "3"):
            print("Invalid choice. Try again.\n")
            heuristic = input("Choose which heuristic to use:\n1. Manhattan-distance\n2. Hamming-distance\n3. Improved Manhattan-distance\n>>> ")
        
        mode = input("Choose which mode to use:\n1. Easy\n2. Hard (NOTE: the algorithm might not find a solution in reasonable time.)\n>>> ")
        while mode not in ("1", "2"):
            print("Invalid choice. Try again.")
            mode = input("Choose which mode to use:\n1. Easy\n2. Hard (NOTE: the algorithm might not find a solution in reasonable time.)\n>>> ")
        
        return heuristic, mode

    def print_end_menu(self):
        """Creates the end menu of the program and asks user's
        choice to continue or exit.

        Returns:
            string: User's choice to continue or exit: "s" or "q".
        """
        choice = input("\nTo return to the start menu press s, to exit press q\n>>> ")
        return choice

    def print_board(self, tile_values):
        """Outputs the board to the console as a string.
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
