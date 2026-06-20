class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1: return strs[0]
        m=0
        M=len(strs[0])
        while True and m<M:
            curr=strs[0][m]
            for s in strs[1:]:
                if m>len(s)-1: return strs[0][:m]
                if s[m]!=curr: return strs[0][:m]
            m+=1
        return strs[0][:m]