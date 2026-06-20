class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for the starting point (m, s_m)
        s_m: column idx
        x_m: right (0,1) or down(1,0)
        => s_{m+1} = s_m + x_m[1]
        f_m(s_m ,x_m)=cost(m,s_m) + f*_{m'}(s_{m+1})
        f*_m(s_m) = min_{x_m}(f_m(s_m, x_m))
        '''

        M=len(grid)
        N=len(grid[0])
        if M==1 or N==1:
            return sum([sum(row) for row in grid])
        
        dp=[[], [sum(grid[-1][i:]) for i in range(N)]]
        print(dp)

        for m in range(M-2, -1,-1):
            dp[0]=[math.inf for _ in range(N)]
            stage_m=dp[0]

            for s_m in range(N-1,-1,-1):
                F=[]
                for x_m in [(0,1),(1,0)]:
                    s_mp1=s_m+x_m[1]
                    mp1=m+x_m[0]
                    F.append((grid[m][s_m] + dp[mp1-m][s_mp1]) if (mp1<M and s_mp1<N ) else math.inf)
                f_min=min(F)
                stage_m[s_m]=f_min
            dp[1]=stage_m
        return dp[0][0]
