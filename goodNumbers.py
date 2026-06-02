class Solution:
    def goodNumbers(self,num):
        MOD=10**9+7
        def power(x,n):
            if n==0:
                return 1
            half=power(x,n//2)
            
            if n%2==0:
                return (half*half)%MOD
            else:
                return (x*half*half)%MOD
        even=(num+1)//2
        odd=num//2
        return (power(5,even)*power(4,odd))%MOD
    
if __name__=='__main__':
    num=int(input('Enter number of indices:'))
    Ashu=Solution()
    print(Ashu.goodNumbers(num))
    