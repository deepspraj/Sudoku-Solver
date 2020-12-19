# Sudoku Solver

The Sudoku Solver is program which is capable of solving any complicated sudoku.

There are two ways to solve the sudoku. They are as follows :

1. The naive approach is to generate all possible configurations of numbers from 1 to 9 to fill all the empty cells (upto 81 cells). The naive is a time consuming approach and perform's (at max 9^81 i.e 1.9662705* 10<sup>77</sup>) operations.

2. The Algorithm we utilised to solve the sudoku is known as **Backtracking Algorithm**.
    
    The Algorithm is as explained below:

    - Pick / find the empty cells or any kind of denotations (whichever programmer have stated).
    - Try all the numbers from 1 to 9 in the first empty cell.
    - Pick the best possible solution and get it placed in that empty cell.
    - Repeat the above 3 steps unless and until last block is too filled with the best possible solution.
    - At some location encountered that no number from 1 to 9 satisfies all the rules of Sudoku game then increment the last filled empty space by 1 and then try for the solution. Even you encountered the same problem then increment the last of that filled element unless and until each and every empty cell is filled.
    - Keep repeating the above process until your solution is a valid solution.
    - Once you solved the Sudoku just print it according to the basic block structure. 

**Always follow the set of rules required to solve the Sudoku Puzzle (The Game).**


<br>

```\sudokuSolver>python sudoku.py```

```0,0,3,0,0,7,0,6,0```

```0,0,7,8,0,0,2,0,0```

```0,0,0,0,0,0,0,3,0```

```0,0,0,0,5,0,0,0,1```

```0,0,5,4,0,8,3,7,9```

```0,3,0,2,7,9,6,4,0```

```5,0,0,0,0,0,0,0,3```

```0,7,6,3,9,4,0,0,0```

```0,0,4,0,0,5,0,8,0```

<br>
Output:

```2 5 3 | 9 4 7 | 1 6 8```

```9 6 7 | 8 3 1 | 2 5 4```

```4 8 1 | 5 6 2 | 9 3 7```

```---------------------```

```7 4 9 | 6 5 3 | 8 2 1```

```6 2 5 | 4 1 8 | 3 7 9```

```1 3 8 | 2 7 9 | 6 4 5```

```---------------------```

```5 1 2 | 7 8 6 | 4 9 3```

```8 7 6 | 3 9 4 | 5 1 2```

```3 9 4 | 1 2 5 | 7 8 6```
