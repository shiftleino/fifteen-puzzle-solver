# Implementation Document

## Project Structure
The project contains two classes that are responsible for the main logic of the program, Game and Solver. The Game-class is responsible for the orchestration of the game such as initialising the starting board of the puzzle, setting the heuristic, and checking if the randomly created puzzle is solvable. The Game-class also creates the Solver-class that is responsible for solving the puzzle. The Solver-class contains the logic for solving the puzzle such as the implementation of the IDA* -algorithm and the implementation of the heristics that are used in the algorithm. The Solver-class focuses only on solving the given starting tile placement with the given heuristic.

In addition, the project contains two classes for the user interface, ConsoleUI and GraphicalUI. ConsoleUI is responsible for printing the console messages for the user and receiving the input of the user. GraphicalUI is responsible for showing the steps the program took to reach the solution.

## Time and Space Complexity
The time complexity of IDA* is hard to analyze from the pseudocode as it depends on how many iterations are run, which in turn depends on how accurate the heuristic function is. However, in worst case the algorithm performs time-wise like the Iterative-Deepening Depth-First-Search (IDDFS), O(b^d) where b is the branching factor and d is the depth of the shallowest solution. In the case of 15 Puzzle the worst-case branching factor is 4 as the blank tile can be moved up, down, left, and right.

The space complexity of IDA* is linear, O(b*d), as we need only space for the current solution path and its expanded nodes.

All the heuristics are of time-complexity O(n^2) where n is the size of the board, 4.

## Limitations and Improvement Topics
The biggest limitation and a possible improvement topic of the project is that none of the heuristics can solve every "hard" puzzle that is produced by the program in reasonable time. This would require a much better heuristics that would use a pre-calculated pattern database. However, I did not find this type of method necessary in the scope of this project as it would lead the focus away from the algorithm which is the core of the project.

## Sources
- Antti Laaksonen, 2021. Tietorakenteet ja algoritmit. Kurssikirja. 
- https://en.m.wikipedia.org/wiki/15_puzzle
- https://en.wikipedia.org/wiki/Iterative_deepening_A*
- https://cseweb.ucsd.edu//~ccalabro/essays/15_puzzle.pdf
- https://en.wikipedia.org/wiki/Parity_of_a_permutation
- https://www.sfu.ca/~mdevos/notes/geom-sym/14_transpositions.pdf
- https://sites.millersville.edu/bikenaga/abstract-algebra-1/permutations/permutations.pdf
- https://michael.kim/blog/puzzle

Some videos:
- [Lecture on IDA*](https://www.youtube.com/watch?v=5LMXQ1NGHwU)
- [Example on how A* works](https://www.youtube.com/watch?v=6TsL96NAZCo)
- [15 Puzzle logic explained](https://www.youtube.com/watch?v=YI1WqYKHi78)
