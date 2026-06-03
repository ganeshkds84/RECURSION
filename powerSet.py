class Solution:
    def powerSet(self,nums):
        final=[]    
        def solve(i,arr,current):
            if i==len(arr):
                final.append(current[:])
                return
            current.append(arr[i])
            solve(i+1,arr,current)
            current.pop()
            solve(i+1,arr,current)
            
        solve(0,nums,[])
        return final
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    Ashu=Solution()
    print(Ashu.powerSet(nums))
    