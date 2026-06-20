class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M=len(s)
        N=len(p)

        if M==0 and N==0:
            return True
        if M==0:
            return all([c=="*" for c in p])
        if N==0:
            return False

        s+="$"
        p+="$"

        dp=[[False for _ in range(N+1)] for _ in range(M+1)]

        m=M
        c1="$"
        dp[-1][-1]=True
        for s_m in range(N-1,-1,-1):
            F=False
            c2=p[s_m]
            if c2=="?":
                False
            elif c2=="*":
                F=F or dp[m][s_m+1]
            else:
                False
            dp[m][s_m]=F

        for m in range(M-1,-1,-1):
            stage_m=dp[m]
            c1=s[m]
            for s_m in range(N-1,-1,-1):
                F=False
                c2=p[s_m]
                if c2=="?":
                    F=F or dp[m+1][s_m+1]
                elif c2=="*":
                    F=F or dp[m+1][s_m+1]
                    F=F or dp[m+1][s_m]
                    F=F or dp[m][s_m+1]
                elif c2==c1:
                    F=F or dp[m+1][s_m+1]
                else:
                    False
                stage_m[s_m]=F
        return dp[0][0]