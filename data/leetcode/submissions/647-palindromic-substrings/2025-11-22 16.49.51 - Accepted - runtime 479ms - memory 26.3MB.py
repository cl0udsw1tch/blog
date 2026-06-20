class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for s[m:s_m]

        '''

        M=len(s)
        N=M

        if M==1:
            return 1
        if M==2:
            return 2 + int(s[0]==s[1])
        
        dp=[[False for _ in range(N)] for _ in range(M)]
        dp[-1][-1]=True

        for m in range(M-2,-1,-1):
            stage_m=dp[m]

            for s_m in range(m,N):
                F=False
                if s_m==m:
                    stage_m[s_m]=True
                    continue
                if s_m==m+1:
                    stage_m[s_m] = s[m]==s[s_m]
                    continue
                if s[s_m]==s[m]:
                    F=dp[m+1][s_m-1]
                stage_m[s_m]=F
        return sum(sum([int(c) for c in row]) for row in dp)