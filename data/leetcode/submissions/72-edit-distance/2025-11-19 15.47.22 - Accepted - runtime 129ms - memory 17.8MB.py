class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for word1[m:], word2[s_m:]
        s_m: index in word2
        x_m: insertion of word2[s_m] at position m  {word1[m:],word2[s_m+1:]}, => C_m = 1
             deletion of word1[m]                   {word1[m+1:],word2[s_m:]}, => C_m = 1
             replacement of word1[m]                {word1[m+1:],word2[s_m+1:]} => C_m = 1
             doing nothing                          {word1[m+1:],word2[s_m+1:]} => C_m = 0
     
        f_m(s_m, x_m) = C_m + f*_m'(s_{m+1})
        f*_m(s_m) = min_{x_m}(f_m(s_m, x_m))

        '''

        M,N=len(word1),len(word2)
        if min(N,M)==0:
            return max(N,M)
        if M==1:
            return int(word1[0] not in word2) + N-1
        if N==1:
            return int(word2[0] not in word1) + M-1

        dp=[[], [int(word1[-1] not in word2[n:]) + (N-n-1) for n in range(N)]]
 
        X=[(1,0), (0,1), (1,1)]

        for m in range(M-2,-1,-1):
            dp[0] = [math.inf for _ in range(N)]
            stage_m=dp[0]
            stage_mp1=dp[1]

            for s_m in range(N-1,-1,-1):
                F=[]
                for x_m in X:
                    s_mp1=s_m+x_m[1]
                    mp=x_m[0]
                    f=1 + (dp[mp][s_mp1] if s_mp1<N else M-(m+1))
                    F.append(f)
                if word1[m]==word2[s_m]:
                    f=dp[1][s_m+1] if s_m+1<N else M-(m+1)
                    F.append(f)
                f_min=min(F)
                stage_m[s_m]=f_min
            
            dp[1]=stage_m

        return dp[1][0]