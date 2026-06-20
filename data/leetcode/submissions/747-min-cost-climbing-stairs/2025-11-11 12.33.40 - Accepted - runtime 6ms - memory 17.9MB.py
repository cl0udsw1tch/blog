class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        stage_n: n=0...N-1 subproblem solves the problem for n...N
        s_n: current step
        x_n: climb 1 or 2 steps
            s_n + x_n = s_{n'} where n'=n+x_n
        f_n(s_n,x_n): cost[s_n] + f*_{n'}(s_{n'})
        f*_n(s_n) = min_{x_n}(f_n(s_n,x_n))

        '''

        N=len(cost)

        dp=[[None], [cost[-2]],[cost[-1]]]

        for n in range(N-3,-1,-1):
            stage_n=dp[0]
            stage_np1=dp[1]
            stage_np2=dp[2]

            s_n=n
            F=[cost[s_n]+stage_np1[0], cost[s_n]+stage_np2[0]]
            f_min=min(F)
            stage_n[0]=f_min

            dp[2]=stage_np1
            dp[1]=stage_n
            dp[0]=[None]
        return min(dp[1][0], dp[2][0])