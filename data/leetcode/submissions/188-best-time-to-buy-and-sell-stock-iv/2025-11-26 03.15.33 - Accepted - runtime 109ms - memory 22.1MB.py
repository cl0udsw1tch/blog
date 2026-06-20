class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        stage_m = 0...M-1 subproblem f*_m(s_m) solves the problem for [m...M-1]
        s_m: havent bought (0), bought 1 (1), sold 1(2), bought 2 (3), sold 2(4) ...
        x_m: buying, selling, or nothing
        (buying) f_m(s_m, x_m) = f*_{m+1}(s_m+1)-prices[m]
        (selling) f_m(s_m, x_m) = f*_{m+1}(s_m-1)+prices[m]
        (nothing) f_m(s_m, x_m) = f*_{m+1}(s_m)

        '''

        M= len(prices)
        dp = [[-float('inf')] * (2*k+1) for _ in range(M)]

        for s_m in range(0,2*k+1,2):
            dp[M-1][s_m]=0
        for s_m in range(1,2*k+1,2):
            dp[M-1][s_m]=prices[M-1]

        for m in range(M-2, -1, -1):
            for s_m in range(2*k+1):
                F = []
                if s_m < 2 * k:
                        F.append(dp[m+1][s_m+1] + (-1 if s_m%2==0 else 1)*prices[m])
                        F.append(dp[m+1][s_m])
                else:
                    F.append(dp[m+1][2*k])

                dp[m][s_m] = max(F)

        return dp[0][0]  