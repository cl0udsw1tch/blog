class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        M=len(t)
        N=len(s)

        if M<N: return False
        if M==1: return s==t
        if N==1: return s in t

        dp=[[False for _ in range(N+1)] for _ in range(M+1)]
        for m in range(M+1):
            dp[m][-1]=True

        for m in range(M-1,-1,-1):
            stage_m=dp[m]
            for s_m in range(N-1,-1,-1):
                F=[]
                f=dp[m+1][s_m]
                F.append(f)
                f=t[m]==s[s_m] and dp[m+1][s_m+1]
                F.append(f)

                f_any=any(F)
                stage_m[s_m]=f_any
        return dp[0][0]