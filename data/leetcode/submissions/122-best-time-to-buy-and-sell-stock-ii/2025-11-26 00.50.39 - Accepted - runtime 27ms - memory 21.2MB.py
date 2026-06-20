class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        stage_m = 0...M-1 subproblem f*_m(s_m) solves the problem for [m...M-1]
        s_m: holding (1) or not (0)
        x_m: buying or selling, or nothing
        (buying) f_m(s_m, x_m) = f*_{m+1}(s_m+1)-prices[m]
        (selling) f_m(s_m, x_m) = f*_{m+1}(s_m-1)+prices[m]
        (nothing) f_m(s_m, x_m) = f*_{m+1}(s_m)

        (holding) f*_m(s_m) = max( f*_{m+1}(0)+prices[m], f*_{m+1}{1})
        (not holding) f*_m(s_m) = max(f*_{m+1}{1}-prices[m], f*_{m+1}(0))

        '''

        M= len(prices)
        dp=[[0,0] for _ in range(M)]

        dp[M-1][0]=0
        dp[M-1][1]=prices[M-1]

        for m in range(M-2, -1,-1):
            for s_m in [0,1]:
                F= []
                for x_m in [-1, 0, 1]:
                    if s_m==0 and x_m==-1: continue
                    if s_m==1 and x_m==1: continue
                    s_mp1=s_m+x_m
                    f=dp[m+1][s_mp1] - x_m*prices[m]
                    F.append(f)
                f_max=max(F)
                dp[m][s_m]=f_max
        return dp[0][0]
