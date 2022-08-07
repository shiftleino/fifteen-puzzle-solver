import copy
import time


class Solver:
    """The Solver-class is responsible for the solving of the Fifteen Puzzle
    using the IDA*-algorithm with two different heuristics: Manhattan-distance
    and Hamming-distance.
    """
    def __init__(self, game):
        self.game = game
        self.heuristic = self.game.get_heuristic()
        self.correct_solution = self.game.get_correct_solution()
        self.start_tile_values = self.game.get_board()
        self.bound = self.get_heuristic_value(self.start_tile_values)
        self.solution_path = [self.start_tile_values]

    def get_blank_position(self, tile_values):
        """Finds the position of the blank tile.

        Args:
            tile_values ([][]int): The placement of the tile values.

        Returns:
            (int, int): The position of the blank tile (row, column).
        """
        for i in range(4):
            for j in range(4):
                if tile_values[i][j] == 16:
                    return (i, j)

    def get_next_boards(self, tile_values):
        """Finds the possible board placements within one move from the given tile values.

        Args:
            tile_values ([][]int): The starting position of the tile values.

        Returns:
            [][][]int: The possible positions within one move from the starting position.
        """
        next_boards = []
        blank_row, blank_col = self.get_blank_position(tile_values)
        if blank_row != 0:
            new_board = copy.deepcopy(tile_values)
            new_board[blank_row - 1][blank_col] = tile_values[blank_row][blank_col]
            new_board[blank_row][blank_col] = tile_values[blank_row - 1][blank_col]
            next_boards.append(new_board)
        if blank_row != 3:
            new_board = copy.deepcopy(tile_values)
            new_board[blank_row + 1][blank_col] = tile_values[blank_row][blank_col]
            new_board[blank_row][blank_col] = tile_values[blank_row + 1][blank_col]
            next_boards.append(new_board)
        if blank_col != 0:
            new_board = copy.deepcopy(tile_values)
            new_board[blank_row][blank_col - 1] = tile_values[blank_row][blank_col]
            new_board[blank_row][blank_col] = tile_values[blank_row][blank_col - 1]
            next_boards.append(new_board)
        if blank_col != 3:
            new_board = copy.deepcopy(tile_values)
            new_board[blank_row][blank_col + 1] = tile_values[blank_row][blank_col]
            new_board[blank_row][blank_col] = tile_values[blank_row][blank_col + 1]
            next_boards.append(new_board)
        return next_boards
    
    def get_heuristic_value(self, tile_values):
        """Calculates the heuristic value of the given board.

        Args:
            tile_values ([][]int): The current board.

        Returns:
            int: The heuristic value.
        """
        if self.heuristic == "manhattan":
            return self.get_manhattan_distance(tile_values)
        elif self.heuristic == "hamming":
            return self.get_hamming_distance(tile_values)

    def get_manhattan_distance(self, tile_values):
        """Calculates the Manhattan-distance of the given board to the correct solution.

        Args:
            tile_values ([][]int): The tile values of the current board.

        Returns:
            int: The Manhattan-distance.
        """
        total_distance = 0
        for i in range(4):
            for j in range(4):
                value = tile_values[i][j]
                correct_row = value // 4
                correct_col = value % 4 - 1
                if value % 4 == 0:
                    correct_row -= 1
                    correct_col = 3
                sub_distance = abs(correct_row - i) + abs(correct_col - j)
                total_distance += sub_distance
        return total_distance

    def get_hamming_distance(self, tile_values):
        """Calculates the Hamming-distance between the given tile values and the correct solution.

        Args:
            tile_values ([][]int): The tile values of the current board.

        Returns:
            int: The Hamming-distance.
        """
        count = 0
        for i in range(4):
            for j in range(4):
                if self.correct_solution[i][j] != tile_values[i][j]:
                    count += 1
        return count

    def search(self, moves):
        """Implements the main logic of the IDA* -algorithm including the depth-first-search.

        Returns:
            int: The minimum estimated cost found using the current bound.
        """
        current_board = self.solution_path[-1]
        if self.heuristic == "manhattan":
            total_cost = moves + self.get_manhattan_distance(current_board)
        elif self.heuristic == "hamming":
            total_cost = moves + self.get_hamming_distance(current_board)
        
        # TODO: REMOVE THESE LOGS WHEN DONE WITH TESTING
        #print(f"\nTotal cost so far: {total_cost}")
        #print(f"Of which heuristic: {self.get_manhattan_distance(current_board)}")
        #print(current_board)
        #time.sleep(1)

        if total_cost > self.bound:
            return total_cost
        if self.check_if_solution(current_board):
            return 0
        minimum_cost = float("inf")
        for next_board in self.get_next_boards(current_board):
            if next_board not in self.solution_path:
                self.solution_path.append(next_board)
                result = self.search(moves + 1)
                if result == 0:
                    return 0
                if result < minimum_cost:
                    minimum_cost = result
                self.solution_path.pop()
        return minimum_cost

    def solve_puzzle(self):
        """Solves the puzzle using IDA* -algorithm. The implementation is based on the pseudocode
        shown in https://en.wikipedia.org/wiki/Iterative_deepening_A*, with minor modifications.

        Returns:
            [][][]int: Returns the found path if found.
        """
        while True:
            result = self.search(moves=0)
            if result == 0:
                return self.solution_path
            if result == float("inf"):
                return None
            self.bound = result

            # TODO: remove this print after testing
            print(f"Current bound: {self.bound}")

    def check_if_solution(self, tile_values):
        """Check if the given tile values match the solution values.

        Returns:
            boolean: If the given tile values are the same as the solution: True or False.
        """
        if tile_values == self.correct_solution:
            return True
        return False
