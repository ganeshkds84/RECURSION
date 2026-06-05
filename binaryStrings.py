class Solution:
    def binaryStrings(self,n):
        ans=[]    
        def solve(current):
            if len(current)==n:
                ans.append(current)
                return
            if len(current)!=n:
                solve(current+'0')
            if not current or current[-1]!='1':
                solve(current+'1')
        solve('')
        ans1=[]
        def solve1(current):
            if len(current)==n:
                ans1.append(current)
                return
            if len(current)!=n:
                solve1(current+'0')
            if len(current)!=n:
                solve1(current+'1')
        solve1('')
        return ans,ans1
                   
if __name__=='__main__':
    n=int(input('Enter the length of the string:'))
    Ashu=Solution()
    print(Ashu.binaryStrings(n))