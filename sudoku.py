import sudokuSolver

board = []

for i in range (9):
    board.append([int(j) for j in input().split(',')])


p1 = sudokuSolver.sudoku(board)
p1.solver()
p1.printBoard()
