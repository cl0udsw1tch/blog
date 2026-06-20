class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        stage_m: m=1...M-1 subproblem f*_m(s_m) solves the problem for text1[m:] and text2[s_m:]
        s_m: index in text2
        x_m: considerig subproblems for {text[m+1:],text2[s_m:]}, {text[m:,text2[s_m+1:]]}, {text1[m+1:], text2{s_m+1:}
        f_m(s_m, x_m) = f*_m'(s_{m+1}) [+int(text1[m]==text2[s_m]) if x_m=(1,1)]
        f*_m(s_m) = max_{x_m}(f_m(s_m, x_m))

        '''

        M,N=len(text1),len(text2)
        if M==1:
            return int(text1[0] in text2)
        if N==1:
            return int(text2[0] in text1)

        dp=[[], [int(text1[M-1] in text2[n:]) for n in range(N)]]
        X=[(1,0), (0,1), (1,1)]

        for m in range(M-2,-1,-1):
            dp[0] = [0 for _ in range(N)]
            stage_m=dp[0]
            stage_mp1=dp[1]

            for s_m in range(N-1,-1,-1):
                F=[]
                for x_m in X:
                    s_mp1=s_m+x_m[1]
                    mp=x_m[0]
                    f=dp[mp][s_mp1] if s_mp1<N else 0
                    if x_m==(1,1):
                        f+=int(text1[m]==text2[s_m])
                    F.append(f)
                f_max=max(F)
                stage_m[s_m]=f_max
            
            dp[1]=stage_m

        return dp[1][0]