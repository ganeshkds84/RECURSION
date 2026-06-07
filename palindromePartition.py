class Solution:
    def palindromePartitioning(self,s):
        result=[]
        def isPalindrome(st):
            l=0
            r=len(st)-1
            while l<r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(index,temp):
            if index==len(s):
                result.append(temp[:])
                return
            for i in range(index,len(s)):
                current=s[index:i+1]
                if isPalindrome(current):
                    temp.append(current)
                    backtrack(i+1,temp)
                    temp.pop()
        backtrack(0,[])
        return result
    
if __name__=='__main__':
    s=input('Enter the string:')
    Ashu=Solution()
    print(Ashu.palindromePartitioning(s))