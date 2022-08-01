import unittest
from entities.solver import Solver
from entities.game import Game
from entities.board import Board

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(self.board)
        self.solver = Solver(self.game)
        self.correct = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    def test_manhattan_distance_correct(self):
        distance = self.solver.get_manhattan_distance(self.correct)
        self.assertEqual(distance, 0)

    def test_manhattan_distance(self):
        board_values = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        distance = self.solver.get_manhattan_distance(board_values)
        self.assertEqual(distance, 32)