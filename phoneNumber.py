class Solution:
    def phoneNumCombo(self,digits):
        if not digits:
            return []
        ans=[]
        mapping={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def solve(index,current):
            if index==len(digits):
                ans.append(current)
                return 
            letters=mapping[digits[index]]
            for ch in letters:
                solve(index+1,current+ch)
        solve(0,'')
        return ans

if __name__=='__main__':
    digits=input('Enter the digts:')
    Ashu=Solution()
    print(Ashu.phoneNumCombo(digits))