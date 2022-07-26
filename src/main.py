from ui.console import ConsoleUI
from entities.board import Board
from entities.game import Game

def main():
    board = Board()
    game = Game(board)
    game.start_game()
    ui = ConsoleUI(board)
    heuristic = ui.create_start_menu()
    while heuristic not in ("1", "2"):
        print("Invalid choice. Restarting game...")
        game.start_game()
        heuristic = ui.create_start_menu()
    game.set_heuristic(heuristic)
    ui.print_board()
    restart_choice = ui.create_end_menu()

    while restart_choice == "s":
        heuristic = ui.create_start_menu()
        while heuristic not in ("1", "2"):
            print("Invalid choice. Restarting game...")
            heuristic = ui.create_start_menu()
        ui.print_board()
        restart_choice = ui.create_end_menu()


if __name__ == "__main__":
    main()
