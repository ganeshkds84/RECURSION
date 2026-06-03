class Ganesh:
    def Ashu(self,n):
        ans=[]
        def wazeey(current,open_count,close_count)    :
            if len(current)==2*n:
                ans.append(current)
            if open_count<n:
                wazeey(current+'(',open_count+1,close_count)
            if close_count<open_count:
                wazeey(current+')',open_count,close_count+1)
        wazeey('',0,0)
        return ans
            
if __name__=='__main__':
    n=int(input('Enter the number of paranthesis required:'))
    Ashwika=Ganesh()
    print(Ashwika.Ashu(n))