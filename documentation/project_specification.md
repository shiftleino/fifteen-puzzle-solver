# Project Specification Document

Documentation and code language: English<br>
Programming language: Python<br>
Peer review programming languages: Python, Go<br>
Degree Programme: Bachelor's Programme in Computer Science<br>

## The Problem: 15 Puzzle
The problem this project tackles is the famous 15 puzzle. In the puzzle the basic idea is to slide 15 square tiles in a 4x4-board (16 total positions) to a position where the tiles are in numerical order from left to right, top to bottom. Naturally, only the tiles that are on the same row or column as the open position are allowed to be moved. The goal of the project is to create an artificial solver that can solve, using specific algorithms, the 15 puzzle efficiently whenever it is solvable.

The problem is solvable only if the parity of the number of moves the blank position moves from starting position to goal position is the same as the parity of the number of transpositions it takes to get from the start permutation to the goal permutation of the board or the parity of the number of inversions there exists in the start permutation.

## Data Structures and Algorithms
As the main algorithm in the solver I have decided to use IDA* (Iterative Deepening A*). IDA* is an algorithm that is a combination of the normal A* algorithm and the traditional iterative deepening depth first search. Instead of the depth of the node, IDA* uses as the value to compare to the threshold the sum of the cost so far to get to the node and heuristic value of the node. As the heuristics I am going to test at least Manhattan distance and Hamming distance. As data structures I will be using stack for the current search path.

I chose this algorithm as it was recommended by the course material but also as 15 puzzle is an interesting problem to test how different heuristics succeed in relation to each other. In addition, many of the potential heuristics one can use to solve this puzzle are admissible, meaning that they underestimate the number of moves left, in other words the cost to the goal. This guarantees that IDA* will eventually find the optimal solution e.g., the smallest amount of slides. It is, however, important to note that the NxN-extension of the 15 puzzle is an NP-hard problem. IDA* is also more efficient with memory usage than standard A*.

As the program uses IDA* as the algorithm, it tries to solve the 15 puzzle in exponential time complexity O(b^m) and linear space complexity O(b*m), where b is the maximum branching factor and m is the maximum depth of the search tree.

## Inputs
The program does not use any inputs provided by the user as the only functionality of the program is to show to the user how it solves the 15 puzzles generated randomly by the computer. In other words, the computer competes with itself in this project.

## Sources
- Antti Laaksonen, 2021. Tietorakenteet ja algoritmit. Kurssikirja. 
- https://en.m.wikipedia.org/wiki/15_puzzle
- https://en.wikipedia.org/wiki/Iterative_deepening_A*
- https://cseweb.ucsd.edu//~ccalabro/essays/15_puzzle.pdf
- https://en.wikipedia.org/wiki/Parity_of_a_permutation
- https://www.sfu.ca/~mdevos/notes/geom-sym/14_transpositions.pdf
- https://sites.millersville.edu/bikenaga/abstract-algebra-1/permutations/permutations.pdf

Some videos:
- [Lecture on IDA*](https://www.youtube.com/watch?v=5LMXQ1NGHwU)
- [Example on how A* works](https://www.youtube.com/watch?v=6TsL96NAZCo)
- [15 Puzzle logic explained](https://www.youtube.com/watch?v=YI1WqYKHi78)