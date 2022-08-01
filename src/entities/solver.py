class Solver:
    """The Solver-class is responsible for the solving of the Fifteen Puzzle
    using the IDA*-algorithm with two different heuristics: Manhattan-distance
    and Hamming-distance.
    """
    def __init__(self, game):
        self.game = game
        self.heuristic = self.game.heuristic
        self.tile_values = self.game.get_board()
        self.bound = self.get_manhattan_distance(self.tile_values)
        self.path = []

    def search(self):
        pass

    def solve_puzzle(self):
        """Solves the puzzle using IDA*-algorithm.

        Returns:
            ([]string, int): Returns the found path and the amount of moves, if found.
        """
        while True:
            result = self.search()
            if result == 0:
                return (self.path, self.bound)
            elif result == -1:
                return (None, -1)
            self.bound = result

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

    def get_hamming_distance(self):
        pass
