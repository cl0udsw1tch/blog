class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0: return 1
        if n==1: return x
        if n==-1: return 1/x
        
        if n<0:
            x=1/x
            n=-n

        if -1e-4<x<1e-4 and n>0: return 0

        if n%2==0:
            return self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, (n+1)//2)/x


