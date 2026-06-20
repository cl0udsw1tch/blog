class Solution:
    def getMoneyAmount(self, n: int) -> int:
        '''
        stage_m: m=1...n subproblem f*_m(s_m) solves the problem for [m....s_m]
        s_m: upperbound
        x_m: which number picked between m and s_m
        f_m(s_m, x_m) = x_m + max(f*_m(x_m-1), f*_{x_m+1}(s_m))
        f*_m(s_m) = min_{x_m}(f_m(s_m, x_m))
        '''

        if n==1: return 0
        if n==2: return 1
        if n==3: return 2

        M=n+1
        dp = [[0 for _ in range(M)] for _ in range(M)]

        for m in range(1, n):
            dp[m][m+1]=m


        for m in range(M-3,0 ,-1):

            for s_m in range(m+2, M):

                F= []
                for x_m in range(m, s_m+1):
                    f=x_m + max(dp[m][x_m-1] if x_m-1>=m else 0, dp[x_m+1][s_m] if x_m+1<=s_m else 0)
                    F.append(f)
                dp[m][s_m]=min(F)

        return dp[1][-1]

        