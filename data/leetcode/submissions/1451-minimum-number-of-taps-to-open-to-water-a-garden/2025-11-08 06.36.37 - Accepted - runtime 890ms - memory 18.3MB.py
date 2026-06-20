class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
   
        stage_m: index m [TAP M]
        s_m: indices spanned by tap m
        x_m: all values such that s_m+x_m is spanned by tap m
            => s_{m+1} = s_m + x_m if s_m+x_m is spanned by tap m+1
        f_m(s_m, x_m) = (x_m != 0) + f*_{m+1}(s_{m+1})
        f*_m(s_m) = optimal way to cover [s_m:n]
        
        '''

        if n==1:
            return ranges[0] or ranges[1]
        dp = [[0 for _ in range(n+1)],[0 for _ in range(n+1)]]
        L=max([0, n-ranges[n]])
        for s_m in range(L, n):
            dp[1][s_m]=1
        for s_m in range(0, L):
            dp[1][s_m]=math.inf
        dp[1][n]=0

        for m in range(n-1,-1,-1):
            stage_mp1=dp[1]
            stage_m=dp[0]
            L=max([0,m-ranges[m]])
            R=min([n, m+ranges[m]])

            f_stars=[0 for _ in range(R-L+1)]
            f_stars[R-L]=stage_mp1[R]
            for x_m in range(R-L-1,-1,-1):
                f_stars[x_m]=min([stage_mp1[L+x_m], f_stars[x_m+1]])

            for s_m in range(L, R+1):
                x_m_star0=s_m-L
                F_star=min([stage_mp1[s_m], (f_stars[x_m_star0+1]+1) if x_m_star0+1<=R-L else math.inf])
                stage_m[s_m]=F_star

            stage_mp1[L:R+1]=stage_m[L:R+1]

        r = dp[1][0] if not math.isinf(dp[1][0]) else -1

        return(r)
     
        
            
                    


        