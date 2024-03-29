# Project Report - Week 2

This week I have started the implementation of the project. I have developed the project iteratively, adding one functionality after another everytime when I need it. The project consists now of four different classes, of which one is empty and one is responsible for the text-based UI. If I have time after completing the game logic I might add also a graphical UI for the project. The other classes that are in a good state are the Game-class and the Board-class. 

In the Game-class I have implemented the initialisation logic of the board where the tile values are formed randomly and the corresponding result is then checked if it is solvable. I tried two different approaches for this check: the number of inversions and the number of transpositions. From these two approaches I decided to use the number of inversions as the implementation was more straight-forward and easier to understand. The implementation for the number of transpositions required a good understanding of permutation theory, and I did not have the time to review these topics in such a way that I could trust the algorithm 100% (it has been two years since last time I studied them). I did however review some basics (sources listed on project specification document) and if the number of inversions implementation is not efficient enough, I might later try to switch to the number of transpositions implementation. In addition to implementing the game logic, I also added unittests to each class. In testing I tried to test basic test cases as well as corner cases.

The hardest part this week was understanding when the 15 puzzle is solvable from the permutation perspective. To understand this I used the theory of [Parity of a permutation](https://en.wikipedia.org/wiki/Parity_of_a_permutation) and the [solvability of the 15 Puzzle](https://en.wikipedia.org/wiki/15_puzzle). I hope the current number of inversions -solution works correctly, at leasts for the test cases it did.

Next week I will dive deep to the IDA*-algorithm and implement the Solver-class.

Approx. number of hours used: 20
