class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        M=len(s)
        if M==1: return 1

        dp=[[0] for _ in range(M)]
        dp[-1][0]=1

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            s_m,s_mp1=0,0
            if ord(s[m])%26 == (ord(s[m+1])-1)%26:
                stage_m[s_m]=stage_mp1[s_mp1]+1
            else:
                stage_m[s_m]=1

        alphabet=[0]*26
        for m in range(M):
            stage_m=dp[m]
            char_m=s[m]
            idx=ord(char_m)-ord('a')
            alphabet[idx]=max(alphabet[idx], stage_m[0])

        return sum(alphabet)
