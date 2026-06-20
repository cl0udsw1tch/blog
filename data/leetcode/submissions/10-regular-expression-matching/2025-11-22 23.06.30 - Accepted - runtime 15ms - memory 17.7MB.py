class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for s[m:], p[s_m:]

        '''

        M=len(s)
        N=len(p)
        s+="$"
        p+="$"
        
        dp=[[False for _ in range(N+1)] for _ in range(M+1)]
        dp[-1][-1] = True

        s1="$"
        m=M
        for s_m in range(N-1,-1,-1):
            s2=p[s_m]
            F=False
            if s_m+1<N:
                if p[s_m+1]=="*":
                    if s2=="*":
                        False
                    else:
                        F=F or dp[M][s_m+2]
                else:
                    False
            else:
                False
            dp[M][s_m]=F

        for m in range(M-1,-1,-1):
            stage_m=dp[m]

            s1=s[m]
            for s_m in range(N-1,-1,-1):
                s2=p[s_m]
                F=False
                if s1==s2 or s2==".":
                    F=F or dp[m+1][s_m+1]
                else:
                    False

                if s_m+1<N:
                    if p[s_m+1] == "*":
                        if s2==s1 or s2==".":
                            F=F or dp[m+1][s_m+2]
                            F=F or dp[m][s_m+2]
                            F=F or dp[m+1][s_m]
                        elif s2=="*":
                            False
                        else:
                            F=F or dp[m][s_m+2]
                    else:
                        False

                stage_m[s_m]=F
   
        return dp[0][0]


        