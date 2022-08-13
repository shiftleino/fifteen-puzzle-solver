import time
from entities.solver import Solver
from entities.game import Game

def set_up(heuristic, mode):
    game = Game()
    game.set_heuristic(heuristic)
    if mode == "easy":
        tile_values = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 11], [13, 14, 15, 12]]
    elif mode == "intermediate":
        tile_values = [[5, 1, 3, 2], [9, 8, 7, 4], [13, 6, 10, 11], [14, 15, 16, 12]]
    game.set_board(tile_values)
    solver = Solver(game)
    return solver

def performance_test_easy():
    print("Average durations:")
    heuristics = [("1", "Manhattan"), ("2", "Hamming"), ("3", "Improved Manhattan")]
    for num, heuristic in heuristics:
        total_time = 0
        for _ in range(100):
            solver = set_up(num, "easy")
            start = time.time()
            solver.solve_puzzle()
            end = time.time()
            sub_time = end - start
            total_time += sub_time

        avg_duration = total_time / 100
        print(f"{heuristic}: {avg_duration:.10f}s")
    print()

def performance_test_intermediate():
    print("Average durations:")
    heuristics = [("1", "Manhattan"), ("2", "Hamming"), ("3", "Improved Manhattan")]
    for num, heuristic in heuristics:
        total_time = 0
        for _ in range(100):
            solver = set_up(num, "intermediate")
            start = time.time()
            solver.solve_puzzle()
            end = time.time()
            sub_time = end - start
            total_time += sub_time

        avg_duration = total_time / 100
        print(f"{heuristic}: {avg_duration:.10f}s")
    print()

def main():
    print("Testing performance with an easy initial board...")
    performance_test_easy()

    print("Testing performance with an intermediate initial board...")
    performance_test_intermediate()


if __name__ == "__main__":
    main()
