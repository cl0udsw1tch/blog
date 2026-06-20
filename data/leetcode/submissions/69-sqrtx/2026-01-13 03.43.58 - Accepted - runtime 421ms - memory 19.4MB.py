class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: return 0
        if x==1: return 1
        if x==2: return 1

        n=2
        while True:
            if n*n > x: break
            n*=2

        for m in range(n//2,n):
            if (m+1)*(m+1)>x: return m