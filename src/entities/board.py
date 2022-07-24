class Board:
    def __init__(self):
        self.tile_values = []

    def fill_board(self, new_tile_values):
        self.tile_values = new_tile_values

    def get_board(self):
        return self.tile_values
        
