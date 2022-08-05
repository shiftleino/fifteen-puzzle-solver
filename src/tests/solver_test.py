import unittest
from entities.solver import Solver
from entities.game import Game
from entities.board import Board

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.board = Board()
        self.game = Game(self.board)
        self.game.start_game()
        self.solver = Solver(self.game)
        self.correct = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    def test_blank_position(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        position = self.solver.get_blank_position(board_values)
        self.assertEqual(position, (2, 1))

    def test_next_boards(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected_result = [
            [[1, 2, 3, 4], [12, 16, 14, 5], [11, 13, 15, 6], [10, 9, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 9, 15, 6], [10, 16, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [16, 11, 15, 6], [10, 9, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 15, 16, 6], [10, 9, 8, 7]]
            ]
        test_result = self.solver.get_next_boards(board_values)
        self.assertEqual(test_result, expected_result)

    def test_next_boards_corner(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 9, 15, 6], [16, 10, 8, 7]]
        expected_result = [
            [[1, 2, 3, 4], [12, 13, 14, 5], [16, 9, 15, 6], [11, 10, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 9, 15, 6], [10, 16, 8, 7]]
            ]
        test_result = self.solver.get_next_boards(board_values)
        self.assertEqual(test_result, expected_result)

    def test_next_boards_side(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [16, 11, 15, 6], [10, 9, 8, 7]]
        expected_result = [
            [[1, 2, 3, 4], [16, 13, 14, 5], [12, 11, 15, 6], [10, 9, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [10, 11, 15, 6], [16, 9, 8, 7]],
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
            ]
        test_result = self.solver.get_next_boards(board_values)
        self.assertEqual(test_result, expected_result)

    def test_manhattan_distance_correct(self):
        distance = self.solver.get_manhattan_distance(self.correct)
        self.assertEqual(distance, 0)

    def test_manhattan_distance(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        distance = self.solver.get_manhattan_distance(board_values)
        self.assertEqual(distance, 32)

    def test_check_correct(self):
        correct = self.solver.check_if_solution(self.correct)
        self.assertEqual(correct, True)

    def test_check_not_correct(self):
        board_values = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
        correct = self.solver.check_if_solution(board_values)
        self.assertEqual(correct, False)

    def test_solve_puzzle_easy_manhattan(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("1")
        self.board.fill_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)
