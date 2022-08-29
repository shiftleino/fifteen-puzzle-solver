import unittest
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.correct = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    def test_get_correct_solution(self):
        result = self.game.correct_solution
        self.assertEqual(result, self.correct)

    def test_set_heuristic_manhattan(self):
        heuristic = "1"
        self.game.heuristic = heuristic
        self.assertEqual(self.game.heuristic, "manhattan")

    def test_set_heuristic_hamming(self):
        heuristic = "2"
        self.game.heuristic = heuristic
        self.assertEqual(self.game.heuristic, "hamming")

    def test_set_improved_manhattan(self):
        heuristic = "3"
        self.game.heuristic = heuristic
        self.assertEqual(self.game.heuristic, "improved_manhattan")

    def test_invalid_heuristic(self):
        heuristic = "4"
        def func():
            self.game.heuristic = heuristic
        self.assertRaises(Exception, func)

    def test_start_game_hard_fills_board(self):
        start_tile_values = self.game.tile_values
        self.assertEqual(start_tile_values, [])
        self.game.start_game_hard()
        end_tile_values = self.game.tile_values
        self.assertEqual(len(end_tile_values), 4)
        self.assertEqual(len(end_tile_values[0]), 4)

    def test_start_game_hard_all_values(self):
        all_values = 16*[True]
        self.game.start_game_hard()
        board_values = self.game.tile_values
        for row in board_values:
            for value in row:
                all_values[value-1] = False
        self.assertEqual(sum(all_values), 0)

    def test_move_blank_up(self):
        expected_board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 16], [13, 14, 15, 12]]
        new_board_values = self.game.move_blank(self.correct, (-1, 0))
        self.assertEqual(new_board_values, expected_board_values)

    def test_move_blank_left(self):
        expected_board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 16, 15]]
        new_board_values = self.game.move_blank(self.correct, (0, -1))
        self.assertEqual(new_board_values, expected_board_values)

    def test_move_blank_illegal(self):
        expected_board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        new_board_values = self.game.move_blank(self.correct, (0, 1))
        self.assertEqual(new_board_values, expected_board_values)

    def test_start_game_easy_fills_board(self):
        start_tile_values = self.game.tile_values
        self.assertEqual(start_tile_values, [])
        self.game.start_game_easy()
        end_tile_values = self.game.tile_values
        self.assertEqual(len(end_tile_values), 4)
        self.assertEqual(len(end_tile_values[0]), 4)

    def test_start_game_easy_all_values(self):
        all_values = 16*[True]
        self.game.start_game_easy()
        board_values = self.game.tile_values
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
        self.game.heuristic = "1"
        self.game.tile_values = board_values
        solution_path, _ = self.game.solve_puzzle()
        self.assertNotEqual(solution_path, None)
