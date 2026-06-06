class Solution:
    def countsubsetSum(self,nums,k):
        self.count=0
        def solve(index,current,total):
            if total==k:
                self.count+=1
                return
            if total>k:
                return
            if index==len(nums):
                return
            current.append(nums[index])
            solve(index+1,current,total+nums[index])
            current.pop()
            solve(index+1,current,total)
        solve(0,[],0)
        return self.count
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    k=int(input('Enter the target value:'))
    Ashu=Solution()
    print(Ashu.countsubsetSum(nums,k))