# Project Report - Week 3

This week I continued to implement the main logic behind the project, mainly the Solver-class. In the Solver-class I managed to implement the IDA*-algorithm for the 15 Puzzle and the current implementation can solve easy versions of the puzzle fast. However, I noticed that the algorithm is very slow when dealing with the randomly shuffled boards and I am not quite sure if it is because of the initialisation of the board still produces unsolvable boards (I hope this is not the case as the method that checks solvability works in tests fine) or that the algorithm is just too slow.

Next week I will try to make the algorithm faster by doing some pruning and maybe changing the Manhattan-heuristic to be more accurate with the estimates. I will also implement the Hamming-distance heuristic. In addition, currently the solver is not added to the main program and the user interface, and therefore I have to do this integration as well.

The hardest part this week was to implement the IDA* -algorithm for the 15 Puzzle. This required many helper functions and comprehensive understanding of what is happening during the search of the algorithm.

Approx. number of hours used: 12
