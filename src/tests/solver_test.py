import unittest
from entities.solver import Solver

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.solver_manhattan = Solver("manhattan")
        self.solver_hamming = Solver("hamming")