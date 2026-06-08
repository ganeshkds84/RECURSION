class Solution:
    def solveSudoku(self, board):
        #your code goes here
        def is_valid(row,col,num):

            for j in range(9):
                if board[row][j]==num:
                    return False
            for i in range(9):
                if board[i][col]==num:
                    return False
            
            start_row=row-row%3
            start_col=col-col%3

            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if board[i][j]==num:
                        return False
            return True

        def solve():

            for i in range(9):
                for j in range(9):

                    if board[i][j]=='.':
                        for num in '123456789':
                            if is_valid(i,j,num):
                                board[i][j]=num
                                if solve():
                                    return True
                                board[i][j]='.'
                        return False
            return True
        solve()
        return board
                        
if __name__=='__main__':
    board = [ ["5", "3", ".", ".", "7", ".", ".", ".", "."] ,
             ["6", ".", ".", "1", "9", "5", ".", ".", "."] ,
             [".", "9", "8", ".", ".", ".", ".", "6", "."] ,
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"] ,
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"] ,
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"] ,
             [".", "6", ".", ".", ".", ".", "2", "8", "."] ,
             [".", ".", ".", "4", "1", "9", ".", ".", "5"] ,
             [".", ".", ".", ".", "8", ".", ".", "7", "9"] ]
    Ashu=Solution()
    print(Ashu.solveSudoku(board))
    