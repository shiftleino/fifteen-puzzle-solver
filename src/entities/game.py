import random


class Game:
    """The Game-class is responsible for the orchestration of the game, including
    setting the starting board and checking if the solution is correct.
    """
    def __init__(self, board):
        self.board = board
        self.correct_solution = [[i + 4*j for i in range(1, 5)] for j in range(4)]
        self.heuristic = ""
        self.blank_position = (3, 3)

    def set_heuristic(self, heuristic):
        """Sets the heuristic the solver will use based on user input.
        "1" is for Manhattan-distance, "2" is for Hamming-distance.

        Args:
            heuristic (string): The heuristic to use in the algorithm: "1" or "2".
        """
        if heuristic == "1":
            self.heuristic = "manhattan"
        else:
            self.heuristic = "hamming"

    def start_game(self):
        """Sets the tile values of the starting board using Random Number Generation.
        """
        solvable = False
        while not solvable:
            used_values = []
            new_tile_values = []
            for _ in range(4):
                row_values = []
                for _ in range(4):
                    tile_value = random.randint(1, 16)
                    while tile_value in used_values:
                        tile_value = random.randint(1, 16)
                    row_values.append(tile_value)
                    used_values.append(tile_value)
                new_tile_values.append(row_values)
            solvable = self.check_if_solvable(new_tile_values)
        
        self.board.fill_board(new_tile_values)

    def check_if_solvable(self, board_values):
        """Checks if the given board is solvable. Board is solvable if the
        parity of the permutation of all 16 tiles is the same as the parity
        of the taxicab distance of the blank tile from its starting position
        to the lower right corner. 

        Args:
            board_values ([][]int): The tile values of the board as a list of lists of integers.

        Returns:
            Boolean: If the board is solvable: True or False.
        """
        perm_parity = blank_parity = 1
        num_transpositions = self.get_number_inversions(board_values)
        if num_transpositions % 2 == 0:
            perm_parity = 2

        blank_distance = self.get_blank_distance(board_values)
        if blank_distance % 2 == 0:
            blank_parity = 2

        return perm_parity == blank_parity

    def get_number_inversions(self, board_values):
        """Finds the number of inversions in the permutation.

        Args:
            board_values ([][]int): The tile values of the board as a list of lists of integers.

        Returns:
            int: The number of inversions.
        """
        count = 0
        flattened_values = [value for row in board_values for value in row]
        for i in range(16):
            for j in range(i + 1, 16):
                if flattened_values[i] > flattened_values[j]:
                    count += 1
        return count

    def get_blank_distance(self, board_values):
        """Finds the taxicab distance of the blank tile from its starting position
        to the lower right corner.

        Args:
            board_values ([][]int): The tile values of the board as a list of lists of integers.

        Returns:
            int: The distance.
        """
        for i in range(3, -1, -1):
            for j in range(3, -1, -1):
                if board_values[i][j] == 16:
                    return (3 - i) + (3 - j)

    def check_if_correct(self):
        """Check if the current board matches the solution of the puzzle.

        Returns:
            Boolean: If the current board is the solution: True or False.
        """
        if self.board.get_board() == self.correct_solution:
            return True
        return False

    def move_blank(self, dx, dy):
        pass

    def get_board(self):
        return self.board.get_board()