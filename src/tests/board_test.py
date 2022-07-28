import unittest
from entities.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_fill_board(self):
        new_tile_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board.fill_board(new_tile_values)
        self.assertEqual(self.board.tile_values, new_tile_values)

    def test_get_board(self):
        new_tile_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board.fill_board(new_tile_values)
        board_values = self.board.get_board()
        self.assertEqual(new_tile_values, board_values)
