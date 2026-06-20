class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem starting at (m, s_m)
        s_m: column index
        x_m: bottom (0) or bottom right (1)
            => s_{m+1} = s_m+x_m
        f_m(s_m, x_m) = triangle[n][s_m] + f*_{m+1}(s_{m+1})
        f*_m(s_m) = min_{x_m} (f_m(s_m, x_m))


        '''

        M=len(triangle)

        if M==1:
            return triangle[0][0]
        if M==2:
            return triangle[0][0]+min(triangle[1])
    
        dp = [[], triangle[-1]]
        X=[0,1]

        for m in range(M-2,-1,-1):
            N=len(triangle[m])
            dp[0]=[0 for _ in range(N)]
            stage_m=dp[0]
            stage_mp1=dp[1]

            for s_m in range(N):
                F=[]
                num_s_m=triangle[m][s_m]
                for x_m in X:
                    s_mp1=s_m+x_m
                    f=num_s_m + stage_mp1[s_mp1]
                    F.append(f)
                f_min=min(F)
                stage_m[s_m]=f_min



            dp[1]=stage_m
        return dp[1][0]


        