import copy


class Solver:
    """The Solver-class is responsible for the solving of the Fifteen Puzzle
    using the IDA*-algorithm with three different heuristics: Manhattan-distance,
    Hamming-distance, and improved Manhattan-distance.
    """
    def __init__(self, game):
        self._game = game
        self._heuristic = self._game.heuristic
        self._correct_solution = self._game.correct_solution
        self._start_tile_values = self._game.tile_values
        self._bound = self.get_heuristic_value(self._start_tile_values)
        self._solution_path = [self._start_tile_values]

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
        raise Exception("Board contains no blank tile.")

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
        if self._heuristic == "manhattan":
            return self.get_manhattan_distance(tile_values)
        if self._heuristic == "hamming":
            return self.get_hamming_distance(tile_values)
        return self.get_improved_manhattan_distance(tile_values)

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
                if self._correct_solution[i][j] != tile_values[i][j]:
                    count += 1
        return count

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
                correct_row = (value - 1) // 4
                correct_col = (value - 1) % 4
                sub_distance = abs(correct_row - i) + abs(correct_col - j)
                total_distance += sub_distance
        return total_distance

    def get_improved_manhattan_distance(self, tile_values):
        """Calculates the improved Manhattan-distance of the given board to the correct solution.
        The function improves the normal Manhattan-distance by taking into account linear conflicts
        in the board e.g., if two values are on the right row but in wrong order. In this case the
        distance is two moves larger.

        Args:
            tile_values ([][]int): The tile values of the current board.

        Returns:
            int: The improved Manhattan-distance.
        """
        total_distance = 0
        for i in range(4):
            row_conflicts = []
            for j in range(4):
                value = tile_values[i][j]
                correct_row = (value - 1) // 4
                correct_col = (value - 1) % 4
                sub_distance = abs(correct_row - i) + abs(correct_col - j)
                total_distance += sub_distance

                if correct_row == i:
                    row_conflicts.append(value)

            for i, first_value in enumerate(row_conflicts):
                for j in range(i+1, len(row_conflicts)):
                    if first_value > row_conflicts[j]:
                        total_distance += 2

        for j in range(4):
            col_conflicts = []
            for i in range(4):
                value = tile_values[i][j]
                correct_col = (value - 1) % 4
                if correct_col == j:
                    col_conflicts.append(value)

            for i, first_value in enumerate(col_conflicts):
                for j in range(i+1, len(col_conflicts)):
                    if first_value > col_conflicts[j]:
                        total_distance += 2

        return total_distance

    def search(self, moves):
        """Implements the main logic of the IDA* -algorithm including the depth-first-search.

        Returns:
            int: The minimum estimated cost found using the current bound.
        """
        current_board = self._solution_path[-1]
        total_cost = moves + self.get_heuristic_value(current_board)

        if total_cost > self._bound:
            return total_cost
        if self.check_if_solution(current_board):
            return 0
        minimum_cost = float("inf")
        for next_board in self.get_next_boards(current_board):
            if next_board not in self._solution_path:
                self._solution_path.append(next_board)
                result = self.search(moves + 1)
                if result == 0:
                    return 0
                if result < minimum_cost:
                    minimum_cost = result
                self._solution_path.pop()
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
                return self._solution_path
            if result == float("inf"):
                return None
            self._bound = result

    def check_if_solution(self, tile_values):
        """Check if the given tile values match the solution values.

        Returns:
            boolean: If the given tile values are the same as the solution: True or False.
        """
        return tile_values == self._correct_solution
