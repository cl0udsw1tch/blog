class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        stage_m: subproblem m=0...n computes # distinct ways to climb to step n starting from m
        s_m: current step
        x_m: climb 1 or 2 steps 
        => s_{m+1} = s_m + x_m
        f_m(s_m, x_m) = # ways to get to n given immediately climbing x_m steps
                      = f*m(s_{m+1})
        f*_m(s_m) = sum_{x_m} f_m(s_m, x_m)


        '''


        dp=[[None],[1],[1]]
        for m in range(n-2,-1,-1):
            stage_m=dp[0]
            stage_mp1=dp[1]
            stage_mp2=dp[2]
            s_m=m
            F=[stage_mp1[0],stage_mp2[0]]
            f_sum=sum(F)
            stage_m[0]=f_sum

            dp[2]=stage_mp1
            dp[1]=stage_m
            dp[0]=[None]
        

        return dp[1][0]
