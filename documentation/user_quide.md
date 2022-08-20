# User Guide

## Commands
First install the requirements when in root of the repository:
```console
pip install -r requirements.txt
`````

To run the program, use the following command when in root of the repository:
```console
python src/main.py
```

To test the program, run the following command when in root of the repository:
```console
pytest src
```

To get the test coverage, run the following command when in root of the repository:
```console
coverage run --branch -m pytest src
```

To get a test coverage report, run the following command after getting the test coverage when in root of the repository:
```console
coverage html
```

## Walkthrough
In the first menu choose which heuristic to use in the solver by typing 1, 2 or 3:
```console
Choose which heuristic to use:
1. Manhattan-distance
2. Hamming-distance
3. Improved Manhattan-distance
>>> 3
```

In the second menu choose the difficulty level of the puzzle. With level "easy" the board is initialized with only 25 moves from the solved position. This should make the puzzle solvable in a short time using every heuristic. With level "hard" every tile is randomly placed in the board in a way that the puzzle is still solvable. This puzzle might take even hours to solve depending on the random placement of the tiles and the chosen heuristic.
```console
Choose which mode to use:
1. Easy
2. Hard (NOTE: the algorithm might not find a solution in reasonable time.)
>>> 1
```

After choosing the difficulty level, the program prints the initial board into the console and starts to solve the puzzle. When the program has solved the puzzle a window is opened for the user to explore the steps the program took to solve the puzzle. By pressing space the user can see the next board in the solution path.

After the user has gone through every board in the solution path, the window closes automatically and the user is asked to exit or continue with a new puzzle. By typing "s" and pressing enter the program will open the start menu. 
```console
To return to the start menu press s, to exit press q
>>> q
```