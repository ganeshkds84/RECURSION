class Solution:
    def myAtoi(self,s):
        s=s.lstrip()    
        if not s:
            return 0
        if s[0]=='-':
            sign=-1
            s=s[1:]
        else:
            sign=1
        def solve(index,num):
            if index>=len(s) or not s[index].isdigit():
                return num
            num=num*10+int(s[index])
            return solve(index+1,num)
        num=solve(0,0)
        m=(2**31)-1
        n=-2**31
        final=num*sign
        if final>m:
            return m
        if final<n:
            return n
        return final
    
if __name__=='__main__':
    s=input('Enter any value:')
    Ashu=Solution()
    print(Ashu.myAtoi(s))
    