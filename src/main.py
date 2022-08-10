from ui.console import ConsoleUI
from entities.game import Game


def main():
    game = Game()
    ui = ConsoleUI()
    start_tile_values = game.start_game()

    heuristic = ui.print_start_menu()
    while heuristic not in ("1", "2", "3"):
        print("Invalid choice. Restarting game...")
        start_tile_values = game.start_game()
        heuristic = ui.print_start_menu()

    game.set_heuristic(heuristic)
    ui.print_start_position(start_tile_values)
    solution_steps, duration = game.solve_puzzle()
    ui.print_solution_steps(solution_steps, duration)
    
    restart_choice = ui.print_end_menu()
    while restart_choice == "s":
        heuristic = ui.print_start_menu()
        while heuristic not in ("1", "2", "3"):
            print("Invalid choice. Restarting game...")
            start_tile_values = game.start_game()
            heuristic = ui.print_start_menu()

        game.set_heuristic(heuristic)
        ui.print_start_position(start_tile_values)
        solution_steps, duration = game.solve_puzzle()
        ui.print_solution_steps(solution_steps, duration)
        restart_choice = ui.print_end_menu()


if __name__ == "__main__":
    main()
