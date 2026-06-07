class Solution:
    def wordSearch(self,board,word):
        rows=len(board)
        cols=len(board[0])
        def dfs(r,c,index):
            print(f'Entered with{r,c}')
            if index==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            if board[r][c]!=word[index]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            print(temp)
            found=(
                dfs(r-1,c,index+1) or
                dfs(r,c+1,index+1) or
                dfs(r+1,c,index+1) or
                dfs(r,c-1,index+1) 
            )
            board[r][c]=temp
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
    
if __name__=='__main__':
    board = [ ["Z", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "B", "E", "E"] ] 
    word = "ABCCED"
    Ashu=Solution()
    print(Ashu.wordSearch(board,word))