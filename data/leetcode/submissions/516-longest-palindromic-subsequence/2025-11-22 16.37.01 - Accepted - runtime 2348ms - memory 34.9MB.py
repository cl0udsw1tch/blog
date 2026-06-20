class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the LCS problem for s[m:] and 
        s[::-1][s_m:]
        

        M=len(s)
        if M==1:
            return 1
        if M==2:
            return 2 if s[0]==s[1] else 1
        
        s_inv=s[::-1]
        N=M
        dp=[[], [1 if s[-1] in s_inv[n:] else 0 for n in range(N)]]

        for m in range(M-2,-1,-1):
            dp[0]=[0 for _ in range(N)]
            stage_m=dp[0]
            stage_mp1=dp[1]

            for s_m in range(N-1,-1,-1):
                F=[]
                for x_m in [(0,1), (1,0)]:
                    s_mp1=s_m+x_m[1]
                    mp=x_m[0]
                    f=dp[mp][s_mp1] if s_mp1<N else 0
                    F.append(f)
                x_m=(1,1)
                mp=x_m[0]
                s_mp1=s_m+x_m[1]
                if s[m]==s_inv[s_m]:
                    f=1+(dp[mp][s_mp1] if s_mp1<N else 0)
                    F.append(f)
                f_max=max(F)
                stage_m[s_m]=f_max
            dp[1]=stage_m
        return dp[1][0]
        '''

        M=len(s)
        N=len(s)
        if M==1:
            return 1
        if M==2:
            return 2 if s[0]==s[1] else 1

        dp=[[0 for _ in range(N)] for _ in range(M)]

        for m in range(M-2,-1,-1):
            stage_m=dp[m]

            for s_m in range(m,N):
                F=[1]
                if s_m==m:
                    stage_m[s_m]=1
                    continue
                if s_m==m+1:
                    stage_m[s_m] = 1 + int(s[m]==s[s_m])
                    continue
                if s[s_m]==s[m]:
                    F.append(2+dp[m+1][s_m-1])
                F.append(max(dp[m][s_m-1], dp[m+1][s_m]))
                f=max(F)
                stage_m[s_m]=f

        return dp[0][-1]
        