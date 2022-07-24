import random

class Game:
    def __init__(self, board):
        self.board = board
        self.correct_solution = [[i + 4*j for i in range(1, 5)] for j in range(4)]

    def restart_game(self):
        solvable = False
        while not solvable:
            new_tile_values = []
            for _ in range(4):
                row_values = []
                for _ in range(4): 
                    tile_value = random.randint(1, 16)
                    row_values.append(tile_value)
                new_tile_values.append(row_values)
            solvable = self.check_if_solvable(new_tile_values)
        
        self.board.fill_board(new_tile_values)

    def check_if_solvable(self, board_values):
        pass

    def check_if_correct(self):
        if self.board.get_board == self.correct_solution:
            return True
        return False