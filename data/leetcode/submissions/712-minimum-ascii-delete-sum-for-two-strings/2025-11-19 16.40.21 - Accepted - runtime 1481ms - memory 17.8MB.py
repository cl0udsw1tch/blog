class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for s1[m:], s2[s_m:]
        s_m: index in s2
        x_m: deletion of s1[m]                   {s1[m+1:],s2[s_m:]}, => C_m = ord(s1[m])
             deletion of s2[s_m]                  {s1[m:],s2[s_m+1:]}, => C_m = ord(s2[s_m])
             doing nothing                        {s1[m+1:],s2[s_m+1:]} => C_m = 0
     
        f_m(s_m, x_m) = C_m + f*_m'(s_{m+1})
        f*_m(s_m) = min_{x_m}(f_m(s_m, x_m))

        '''
        ordStr = lambda s : sum([ord(c) for c in s])
        M,N=len(s1),len(s2)
        if M==1:
            if s1[0] not in s2: return ordStr(s1+s2)
            return ordStr(s2)-ord(s1[0])
        if N==1:
            if s2[0] not in s1: return ordStr(s1+s2)
            return ordStr(s1)-ord(s2[0])

        dp=[[], [ordStr(s2[n:]+s1[-1]) if s1[-1] not in s2[n:] else ordStr(s2[n:])-ord(s1[-1]) for n in range(N)]]
 
        X=[(1,0), (0,1), (1,1)]

        for m in range(M-2,-1,-1):
            dp[0] = [math.inf for _ in range(N)]
            stage_m=dp[0]
            stage_mp1=dp[1]

            for s_m in range(N-1,-1,-1):
                F=[]
                for x_m in X[:2]:
                    s_mp1=s_m+x_m[1]
                    mp=x_m[0]
                    c=ordStr([s2[s_m],s1[m]][x_m[0]])
                    f=c+ (dp[mp][s_mp1] if s_mp1<N else ordStr(s1[mp:]))
                    F.append(f)
                if s1[m]==s2[s_m]:
                    f=dp[1][s_m+1] if s_m+1<N else ordStr(s1[m+1:])
                    F.append(f)
                f_min=min(F)
                stage_m[s_m]=f_min
            
            dp[1]=stage_m

        return dp[1][0]
        