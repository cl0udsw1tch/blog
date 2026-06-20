class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1==str2: return str1
        a,b=(str1,str2) if len(str1)<len(str2) else (str2,str1)
        M,N=len(a),len(b)

        for m in range(M,0,-1):
            if M%m or N%m: continue
            x,y=M//m,N//m
            if a[:m]*x==a and a[:m]*y==b: return a[:m]
        return ""

        
