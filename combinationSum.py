class Solution:
    def cobinationSum(self,nums,target):
        if min(nums)>target:
            return []
        ans=[]
        def solve(index,current,total):
            if total==target:
                ans.append(current[:])
                return
            if total>target:
                return
            if index==len(nums):
                return
            current.append(nums[index])
            solve(index,current,total+nums[index])
            current.pop()
            solve(index+1,current,total)
        solve(0,[],0)
        return ans
            
if __name__=='__main__':
    target=int(input('Enter the target value:'))
    nums=list(map(int,input('Enter the numbers:').split()))
    Ashu=Solution()
    print(Ashu.cobinationSum(nums,target))