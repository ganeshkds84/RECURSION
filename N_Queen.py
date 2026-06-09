class Solution:
    def solveNQueen(self,n):
        res=[]
        cols=set()
        diag=set()
        anti_diag=set()
        board=[['.' for _ in range(n)] for _ in range(n)]
        
        def backtrack(row):
            
            if row==n:
                solution=[]
                for r in board:
                    solution.append(''.join(r))
                res.append(solution)
                
            for col in range(n):
                
                if col in cols:
                    continue
                if (row-col) in diag:
                    continue
                if row+col in anti_diag:
                    continue
                
                board[row][col]='Q'
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                
                backtrack(row+1)
                
                board[row][col]='.'
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
                
        backtrack(0)
        return res

if __name__=='__main__':
    n=int(input('''Enter the 'n' value:'''))
    Ashu=Solution()
    print(Ashu.solveNQueen(n))