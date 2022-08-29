import random
import copy
from time import time
from entities.solver import Solver

class Game:
    """The Game-class is responsible for the orchestration of the game, including
    setting the starting board and checking if the solution is correct.
    """
    def __init__(self):
        self._tile_values = []
        self._correct_solution = [[i + 4*j for i in range(1, 5)] for j in range(4)]
        self._heuristic = ""
        self._blank_position = (3, 3)

    @property
    def tile_values(self):
        """
        Returns:
            [][]int: The current tile values of the board.
        """
        return self._tile_values

    @tile_values.setter
    def tile_values(self, new_tile_values):
        self._tile_values = new_tile_values

    @property
    def correct_solution(self):
        """
        Returns:
            [][]int: The solution board to the puzzle. Read-only.
        """
        return self._correct_solution

    @property
    def heuristic(self):
        """
        Returns:
            string: The current heuristic. When modifying use "1" for Manhattan-distance,
            "2" for Hamming-distance, and "3" for improved Manhattan-distance.
        """
        return self._heuristic

    @heuristic.setter
    def heuristic(self, new_heuristic):
        if new_heuristic == "1":
            self._heuristic = "manhattan"
        elif new_heuristic == "2":
            self._heuristic = "hamming"
        elif new_heuristic == "3":
            self._heuristic = "improved_manhattan"
        else:
            raise Exception("Unkown option for heuristic.")

    def move_blank(self, tile_values, direction):
        """Changes the position of the blank tile in the board to the direction
        given as a parameter (if possible).

        Args:
            tile_values ([][]int): The current board.
            direction ((int, int)): The values to add to the blank tile position (row, column).

        Returns:
            [][]int: The board after moving the blank (if possible).
        """
        new_blank_row = self._blank_position[0] + direction[0]
        new_blank_col = self._blank_position[1] + direction[1]
        if 0 <= new_blank_row <= 3 and 0 <= new_blank_col <= 3:
            tile_values[new_blank_row][new_blank_col], tile_values[self._blank_position[0]][self._blank_position[1]] = tile_values[self._blank_position[0]][self._blank_position[1]], tile_values[new_blank_row][new_blank_col]
            self._blank_position = (new_blank_row, new_blank_col)
        return tile_values

    def start_game_easy(self):
        """Sets the tile values of the starting board using 25 moves from solved board.
        """
        new_tile_values = copy.deepcopy(self.correct_solution)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for _ in range(25):
            next_direction = random.choice(directions)
            new_tile_values = self.move_blank(new_tile_values, next_direction)

        self.tile_values = new_tile_values

    def start_game_hard(self):
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

        self.tile_values = new_tile_values

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
        for i in range(15):
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
        return 0

    def solve_puzzle(self):
        """Solves the puzzle using Solver-class.

        Returns:
            [][][]int, float: The optimal steps the solver took to reach the solution
                              and the time it took.
        """
        solver = Solver(self)
        start_time = time()
        print("Solving...")
        solution_steps = solver.solve_puzzle()
        end_time = time()
        duration = end_time - start_time
        return solution_steps, duration
