class Solution:
    def combinationSum2(self,nums,target):
        nums.sort()
        if nums[0]>target:
            return []
        ans=[]
        def solve(index,current,total):
            if total == target:
                ans.append(current[:])
                return
            if total>target:
                return
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                solve(i+1,
                      current,
                      total+nums[i])
                current.pop()
        solve(0,[],0)
        return ans
           
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    target=int(input('Enter the target value:'))
    Ashu=Solution()
    print(Ashu.combinationSum2(nums,target))