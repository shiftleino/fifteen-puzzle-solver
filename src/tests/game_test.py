import unittest
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.correct = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    def test_get_board(self):
        self.game.set_board(self.correct)
        result = self.game.get_board()
        self.assertEqual(result, self.correct)

    def test_get_correct_solution(self):
        result = self.game.get_correct_solution()
        self.assertEqual(result, self.correct)

    def test_get_heuristic(self):
        heuristic = "2"
        self.game.heuristic = heuristic
        result = self.game.get_heuristic()
        self.assertEqual(result, heuristic)

    def test_set_heuristic_manhattan(self):
        heuristic = "1"
        self.game.set_heuristic(heuristic)
        self.assertEqual(self.game.heuristic, "manhattan")

    def test_set_heuristic_hamming(self):
        heuristic = "2"
        self.game.set_heuristic(heuristic)
        self.assertEqual(self.game.heuristic, "hamming")

    def test_start_game_fills_board(self):
        start_tile_values = self.game.get_board()
        self.assertEqual(start_tile_values, [])
        self.game.start_game()
        end_tile_values = self.game.get_board()
        self.assertEqual(len(end_tile_values), 4)
        self.assertEqual(len(end_tile_values[0]), 4)

    def test_start_game_all_values(self):
        all_values = 16*[True]
        self.game.start_game()
        board_values = self.game.get_board()
        for row in board_values:
            for value in row:
                all_values[value-1] = False
        self.assertEqual(sum(all_values), 0)

    def test_check_solvable(self):
        solvable = self.game.check_if_solvable(self.correct)
        self.assertEqual(solvable, True)
        board_values2 = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        solvable2 = self.game.check_if_solvable(board_values2)
        self.assertEqual(solvable2, True)
        board_values3 = [[12, 10, 15, 2], [6, 13, 1, 8], [7, 16, 14, 4], [5, 9, 11, 3]]
        solvable3 = self.game.check_if_solvable(board_values3)
        self.assertEqual(solvable3, True)

    def test_check_not_solvable(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 16]]
        solvable = self.game.check_if_solvable(board_values)
        self.assertEqual(solvable, False)
        board_values2 = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 16]]
        solvable2 = self.game.check_if_solvable(board_values2)
        self.assertEqual(solvable2, False)

    def test_no_inversions(self):
        inversions = self.game.get_number_inversions(self.correct)
        self.assertEqual(inversions, 0)

    def test_number_inversions(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        inversions = self.game.get_number_inversions(board_values)
        self.assertEqual(inversions, 43)

    def test_blank_distance_same(self):
        distance = self.game.get_blank_distance(self.correct)
        self.assertEqual(distance, 0)

    def test_blank_distance(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        distance = self.game.get_blank_distance(board_values)
        self.assertEqual(distance, 3)

    def test_solve_puzzle(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("1")
        self.game.set_board(board_values)
        solution_path, _ = self.game.solve_puzzle()
        self.assertNotEqual(solution_path, None)
