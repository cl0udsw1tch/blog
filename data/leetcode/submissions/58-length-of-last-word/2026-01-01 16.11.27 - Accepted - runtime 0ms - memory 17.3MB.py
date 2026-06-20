class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        M=len(s)-1
        while s[M]==" ":
            M-=1
        t=0
        for m in range(M,-1,-1):
            if s[m]==" ": break
            t+=1
        return t