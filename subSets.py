class Solution:
    def subsetsWithNoDup(self,nums):
        ans=[]
        nums.sort()
        def solve(index,current):
            ans.append(current[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                solve(i+1,current)
                current.pop()
        solve(0,[])
        return ans
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    Ashu=Solution()
    print(Ashu.subsetsWithNoDup(nums))