class Solution:
    def combinationSum(self,n,k):
        ans=[]    
        nums=[1,2,3,4,5,6,7,8,9]
        def solve(index,current):
            if sum(current)>n:
                return
            if len(current)==k:
                if sum(current)==n:
                    ans.append(current[:])
                return
            if index==len(nums):
                return
            current.append(nums[index])
            solve(index+1,
                  current)
            current.pop()
            solve(index+1,
                  current)
        solve(0,[])
        return ans
    
if __name__=='__main__':
    n=int(input('Enter the target value:'))
    k=int(input('Enter number of numbers to be used:'))
    Ashu=Solution()
    print(Ashu.combinationSum(n,k))
    