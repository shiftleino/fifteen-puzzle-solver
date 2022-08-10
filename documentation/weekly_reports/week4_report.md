# Project Report - Week 4

This week I have integrated the Solver-class to the main loop of the game and refactored the implementation of the algorithm to be more efficient. I have also added a new heuristic method to the program as the previous two (Manhattan and Hamming) didn't manage to solve the puzzle in reasonable time. This new heuristic method is an improved version of the Manhattan-distance and it takes into account the cases where two tiles are in wrong order but on the correct row/column (linear conflict). In addition, I have removed the Board-class as it became redundant when developing the Solver-class and Game-class further. This change also made the dependencies between the classes more logical. During the week I also continued with the documentation.

The hardest part this week was getting the algorithm to solve the randomly produced initial placements. With the easy initial placements the algorithm did great but as the tiles were shuffled randomly on the board the algorithm did not find the solution in sensible time.

Approx. number of hours used: 12
