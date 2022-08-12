from ui.console import ConsoleUI
from entities.game import Game


def run_game(game, ui):
    heuristic, mode = ui.print_start_menu()
    game.set_heuristic(heuristic)
    if mode == "1":
        start_tile_values = game.start_game_easy()
    else:
        start_tile_values = game.start_game_hard()

    ui.print_start_position(start_tile_values)
    solution_steps, duration = game.solve_puzzle()
    ui.print_solution_steps(solution_steps, duration)
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
