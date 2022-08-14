from ui.console import ConsoleUI
from entities.game import Game
from ui import gui


def run_game(game, ui):
    heuristic, mode = ui.print_start_menu()
    game.set_heuristic(heuristic)
    if mode == "1":
        start_tile_values = game.start_game_easy()
    else:
        start_tile_values = game.start_game_hard()

    ui.print_start_position(start_tile_values)
    solution_steps, duration = game.solve_puzzle()
    print(f"\nA solution to the puzzle was found in {duration:.5f} seconds, showing the optimal steps...\n")
    gui.show_solution(solution_steps)
    restart_choice = ui.print_end_menu()
    return restart_choice

def main():
    game = Game()
    ui = ConsoleUI()
    restart_choice = "s"
    
    while restart_choice == "s":
        restart_choice = run_game(game, ui)


if __name__ == "__main__":
    main()
