import unittest
from entities.solver import Solver
from entities.game import Game

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.game = Game()
        self.game.start_game_hard()
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

    def test_hamming_distance(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        distance = self.solver.get_hamming_distance(board_values)
        self.assertEqual(distance, 12)

    def test_hamming_distance_correct(self):
        distance = self.solver.get_hamming_distance(self.correct)
        self.assertEqual(distance, 0)

    def test_improved_manhattan_distance(self):
        board_values = [[4, 2, 7, 8], [1, 6, 3, 5], [11, 13, 15, 16], [10, 9, 12, 14]]
        manhattan_distance = self.solver.get_manhattan_distance(board_values)
        improved_manhattan_distance = self.solver.get_improved_manhattan_distance(board_values)
        conflict_distance = improved_manhattan_distance - manhattan_distance
        self.assertEqual(conflict_distance, 2*3)

    def test_get_heuristic_value(self):
        self.game.set_heuristic("2")
        solver = Solver(self.game)
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        distance = solver.get_heuristic_value(board_values)
        self.assertEqual(distance, 12)

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
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_easy_hamming(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("2")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_easy_improved_manhattan(self):
        board_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("3")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_intermediate_manhattan(self):
        board_values = [[1, 7, 2, 4], [5, 16, 3, 8], [9, 6, 10, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("1")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_intermediate_hamming(self):
        board_values = [[1, 7, 2, 4], [5, 16, 3, 8], [9, 6, 10, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("2")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_intermediate_imporoved_manhattan(self):
        board_values = [[1, 7, 2, 4], [5, 16, 3, 8], [9, 6, 10, 11], [13, 14, 15, 12]]
        self.game.set_heuristic("3")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)

    def test_solve_puzzle_hard_improved_manhattan(self):
        board_values = [[12, 10, 15, 2], [6, 1, 16, 8], [7, 13, 14, 4], [5, 9, 11, 3]]
        self.game.set_heuristic("3")
        self.game.set_board(board_values)
        self.solver = Solver(self.game)
        solution_path = self.solver.solve_puzzle()
        self.assertNotEqual(solution_path, None)
