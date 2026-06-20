class Solution:
    def convert(self, s: str, numRows: int) -> str:

        M=len(s)
        if M==1 or numRows==1:
            return s
        rows=["" for _ in range(numRows)]

        i,j=0,0
        for m in range(M):
            rows[i]+=s[m]
            if i<numRows-1 and j%(numRows-1)==0:
                i+=1
            elif 0<i<numRows:
                i-=1
                j+=1
        return "".join(rows)
        
        