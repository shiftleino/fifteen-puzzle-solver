import random
from time import time
from entities.solver import Solver

class Game:
    """The Game-class is responsible for the orchestration of the game, including
    setting the starting board and checking if the solution is correct.
    """
    def __init__(self):
        self.tile_values = []
        self.correct_solution = [[i + 4*j for i in range(1, 5)] for j in range(4)]
        self.heuristic = ""
        self.blank_position = (3, 3)

    def get_heuristic(self):
        """
        Returns:
            string: The current heuristic.
        """
        return self.heuristic

    def get_correct_solution(self):
        """
        Returns:
            [][]int: The solution board to the puzzle.
        """
        return self.correct_solution

    def get_board(self):
        """
        Returns:
            [][]int: The current tile values of the board.
        """
        return self.tile_values

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

    def set_board(self, tile_values):
        """Sets the current board to the given tile values.

        Args:
            tile_values ([][]int): New tile values for the board.
        """
        self.tile_values = tile_values

    def start_game(self):
        """Sets the tile values of the starting board using Random Number Generation.

        Returns:
            [][]int: The starting tile values.
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

        self.set_board(new_tile_values)
        return new_tile_values

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

    def solve_puzzle(self):
        """Solves the puzzle using Solver-class.

        Returns:
            [][][]int, float: The optimal steps the solver took to reach the solution
                              and the time it took.
        """
        solver = Solver(self)
        start_time = time()
        solution_steps = solver.solve_puzzle()
        end_time = time()
        duration = end_time - start_time
        return solution_steps, duration
