class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        stage_m = 0...M-1 subproblem f*_m(s_m) solves the problem for [m...M-1]
        s_m: havent bought (0), bought (1), sold (2)
        x_m: buying, selling, or nothing
        (buying) f_m(s_m, x_m) = f*_{m+1}(s_m+1)-prices[m]
        (selling) f_m(s_m, x_m) = f*_{m+1}(s_m-1)+prices[m]
        (nothing) f_m(s_m, x_m) = f*_{m+1}(s_m)

        (havent-bought) f*_m(s_m) = max(f*_{m+1}{1}-prices[m], f*_{m+1}(0))
        (bought) f*_m(s_m) = max( f*_{m+1}(0)+prices[m], f*_{m+1}{1})
        (sold) f*_m(s_m) = f*_{m+1}(0)
        

        '''

        M= len(prices)
        dp = [[-float('inf')] * 3 for _ in range(M)]

        dp[M-1][0] = 0                # not bought yet
        dp[M-1][1] = prices[M-1]      # holding a stock
        dp[M-1][2] = 0                # already sold

        for m in range(M-2, -1, -1):
            for s_m in [0,1,2]:
                F = []

                if s_m == 0: 
                    F.append(dp[m+1][1] - prices[m])
                    F.append(dp[m+1][0])
                elif s_m == 1:
                    F.append(dp[m+1][2] + prices[m])
                    F.append(dp[m+1][1])
                elif s_m == 2:  
                    F.append(dp[m+1][2])

                dp[m][s_m] = max(F)

        return dp[0][0]  


        