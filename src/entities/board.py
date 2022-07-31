class Board:
    """The Board-class is responsible for updating the tile values and saving the
    current state of the board.
    """
    def __init__(self):
        self.tile_values = []

    def fill_board(self, new_tile_values):
        """Fills the board with the given tile values.

        Args:
            new_tile_values ([][]int): The tile values to fill the board.
        """
        self.tile_values = new_tile_values

    def get_board(self):
        """
        Returns:
            [][]int: The current tile values of the board.
        """
        return self.tile_values

    def get_blank_position(self):
        for i in range(4):
            for j in range(4):
                if self.tile_values[i][j] == 16:
                    return (i, j)
