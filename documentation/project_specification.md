# Project Specification Document

Documentation and code language: English<br>
Programming language: Python<br>
Peer review programming languages: Python, Go<br>
Degree Programme: Bachelor's Programme in Computer Science<br>

## The Problem: 15 Puzzle
The problem this project tackles is the famous 15 puzzle. In the puzzle the basic idea is to slide 15 square tiles in a 4x4-board (16 total positions) to a position where the tiles are in numerical order. Naturally, only the tiles that are on the same row or column as the open position are allowed to be moved. The goal of the project is to create an artificial solver that can solve, using specific algorithms, the 15 puzzle efficiently whenever it is solvable.

The problem is solvable only if the parity of the number of moves the blank position moves from starting position to goal position is the same as the parity of the number of transpositions it takes to get from the start permutation to the goal permutation of the board.

## Data Structures and Algorithms
As the main algorithm in the solver I have decided to use IDA* (Iterative Deepening A*).

I chose this algorithm as 15 puzzle is an interesting problem to test how different heuristics succeed. In addition, many of the potential heuristics one can use to solve this puzzle are admissible, meaning that they never overestimate the number of moves left. This guarantees that IDA* will eventually find the optimal solution e.g., the smallest amount of slides. It is, however, important to note that the NxN-extension of the 15 puzzle is an NP-hard problem.

The program tries to solve the 15 puzzle in O(n^3) time complexity and O(n) space complexity.

## Inputs
The program does not use any inputs provided by the user as the only functionality of the program is to show to the user how it solves the 15 puzzles generated randomly by the computer. In other words, the computer competes with itself in this project.

## Sources
- https://en.m.wikipedia.org/wiki/15_puzzle
- https://en.wikipedia.org/wiki/Iterative_deepening_A*
- https://cseweb.ucsd.edu//~ccalabro/essays/15_puzzle.pdf