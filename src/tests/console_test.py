import unittest
from ui.console import ConsoleUI

class TestConsoleUI(unittest.TestCase):
    def setUp(self):
        self.console_ui = ConsoleUI()

    def test_start_menu(self):
        result = self.console_ui.create_start_menu()
        self.assertEqual(result, "Fifteen Puzzle Solver")

