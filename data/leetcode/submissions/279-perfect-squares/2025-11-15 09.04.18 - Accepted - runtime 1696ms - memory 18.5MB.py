class Solution:
    def numSquares(self, n: int) -> int:
        '''
        stage_m: m=0...n subproblem f*_m() solves the problem for m
        s_m: {m}
        x_m: any feasible square
            => s_m'=s_m-x_m
        f_m(s_m, x_m) = f*_{m-x_m}(s_m') + 1
        f*_m(s_m) =  \min (f*_{m-x_m}(s_m')) + 1
        f*_m= min_{x_m}(f*_{m-x_m}) + 1
        '''
        if n<=3: return n

        dp=[[0] for _ in range(n+1)]
        
        for m in range(1, n+1):
            stage_m=dp[m]
            s_m=m
            stage_m[0]=min([dp[m-x_m**2][0]+1 for x_m in range(1,int(math.sqrt(m))+1)])
        return dp[n][0]


    

