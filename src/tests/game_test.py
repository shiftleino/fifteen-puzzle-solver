import unittest
from entities.game import Game
from entities.board import Board

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(self.board)

    def test_set_heuristic_manhattan(self):
        heuristic = "1"
        self.game.set_heuristic(heuristic)
        self.assertEqual(self.game.heuristic, "manhattan")

    def test_set_heuristic_hamming(self):
        heuristic = "2"
        self.game.set_heuristic(heuristic)
        self.assertEqual(self.game.heuristic, "hamming")

    def test_start_game_fills_board(self):
        start_tile_values = self.board.get_board()
        self.assertEqual(start_tile_values, [])
        self.game.start_game()
        end_tile_values = self.board.get_board()
        self.assertEqual(len(end_tile_values), 4)
        self.assertEqual(len(end_tile_values[0]), 4)

    def test_start_game_all_values(self):
        all_values = 16*[True]
        self.game.start_game()
        board_values = self.board.get_board()
        for row in board_values:
            for value in row:
                all_values[value-1] = False
        self.assertEqual(sum(all_values), 0)

    def test_check_solvable(self):
        pass

    def test_check_not_solvable(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 16]]
        solvable = self.game.check_if_solvable(board_values)
        self.assertEqual(solvable, False)

    def test_check_correct(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board.fill_board(board_values)
        correct = self.game.check_if_correct()
        self.assertEqual(correct, True)

    def test_check_not_correct(self):
        board_values = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
        self.board.fill_board(board_values)
        correct = self.game.check_if_correct()
        self.assertEqual(correct, False)
