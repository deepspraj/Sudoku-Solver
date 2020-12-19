class sudoku:

    def __init__(self,board):
        self.board = board

    def emptySpaces(self):

        for i in range (9):
            for j in range (9):
                if (self.board[i][j] == 0):
                    return [i, j] #Row, Column

        return None

    def solver(self):

        location = self.emptySpaces() #Location of empty space in terms of [row,col]

        if not location:
            return True
        else:
            row, col = location[0], location[1]

        for i in range (1,10):
            if(self.validator(i,[row,col])):
                self.board[row][col] = i

                if(self.solver()):
                    return True
                
                self.board[row][col] = 0

    def validator(self, number, position):

        #Check Row
        for i in range (9):
            if(self.board[position[0]][i] == number) and (position[1] != i):
                return False

        #Check Column
        for i in range (9):
            if(self.board[i][position[1]] == number) and (position[0] != i):
                return False
              
        
        #Check Particular Box
        locaX = position[1]  // 3     #Location of X
        locaY = position[0]  // 3     #Location of Y

        for i in range (locaY*3, locaY*3 + 3):
            for j in range (locaX*3, locaX*3 + 3):
                if ((self.board[i][j] == number) and (i,j != position)):
                    return False

        return True
        
    def printBoard(self):
        print()
        for i in range (1,10):
            for j in range (1,10):
                if((j%3 == 0) and (j != 9)):
                    print(self.board[i-1][j-1], end=' | ')
                else:
                    print(self.board[i-1][j-1], end=' ')

            if((i%3 == 0) and (i != 9)):
                print('\n---------------------')
            else:
                print()
