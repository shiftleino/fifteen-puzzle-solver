from ui.console import ConsoleUI
from ui.gui import GraphicalUI
from entities.game import Game


def main():
    game = Game()
    user_interface = ConsoleUI()
    gui = GraphicalUI()
    user_interface.run_game(game, gui)


if __name__ == "__main__":
    main()
