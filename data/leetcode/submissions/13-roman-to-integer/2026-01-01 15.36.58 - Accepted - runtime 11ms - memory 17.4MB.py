class Solution:
    def romanToInt(self, s: str) -> int:
        map={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        M=len(s)
        if M==1: return map[s]
        total,m=0,0
        while m < M:
            if m+1<M and map[s[m+1]]>map[s[m]]:
                total+=map[s[m+1]] - map[s[m]]
                m+=2
            else:
                total+=map[s[m]]
                m+=1
        return total