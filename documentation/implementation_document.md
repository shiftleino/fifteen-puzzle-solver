# Implementation Document

## Project Structure
The project contains two classes that are responsible for the main logic of the program, Game and Solver. The Game-class is responsible for the orchestration of the game such as initialising the starting board of the puzzle, setting the heuristic, and checking if the randomly created puzzle is solvable. The Game-class also creates the Solver-class that is responsible for solving the puzzle. The Solver-class contains the logic for solving the puzzle such as the implementation of the IDA* -algorithm and the implementation of the heristics that are used in the algorithm. The Solver-class focuses only on solving the given starting tile placement with the given heuristic, and is therefore developed using single-responsibility-principle.

In addition, the project contains one class for the text-based user interface, ConsoleUI. The program structure allows also the addition of a graphical user interface as the game logic is separated from the user interface.

## Time and Space Complexity


## Performance and O-analysis Comparison


## Limitations and Improvement Topics


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
