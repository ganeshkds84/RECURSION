class Solution:
    def myPow(self,x,n):
        def power(x,n):
            if n==0:
                return 1
            half=power(x,n//2)
            
            if n%2==0:
                return half*half
            else:
                return x*half*half
        if n<0:
            return 1/power(x,-n)
        
        return power(x,n)
    
if __name__=='__main__':
    x=float(input('Enter the number:'))
    n=int(input('Enter the exponent value:'))
    
    Ashu=Solution()
    print(Ashu.myPow(x,n))