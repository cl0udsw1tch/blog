class states:
    PRE_BOUGHT  =0
    BOUGHT_1    =1
    SOLD_1      =2
    BOUGHT_2    =3
    SOLD_2      =4

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        stage_m = 0...M-1 subproblem f*_m(s_m) solves the problem for [m...M-1]
        s_m: havent bought (0), bought 1 (1), sold 1(2), bought 2 (3), sold 2(4)
        x_m: buying, selling, or nothing
        (buying) f_m(s_m, x_m) = f*_{m+1}(s_m+1)-prices[m]
        (selling) f_m(s_m, x_m) = f*_{m+1}(s_m-1)+prices[m]
        (nothing) f_m(s_m, x_m) = f*_{m+1}(s_m)

        '''

        M= len(prices)
        dp = [[-float('inf')] * 5 for _ in range(M)]

        dp[M-1][states.PRE_BOUGHT] = 0          
        dp[M-1][states.BOUGHT_1] = prices[M-1]    
        dp[M-1][states.SOLD_1] = 0               
        dp[M-1][states.BOUGHT_2] = prices[M-1]                 
        dp[M-1][states.SOLD_2] = 0

        for m in range(M-2, -1, -1):
            for s_m in [0,1,2,3,4]:
                F = []
                match s_m:
                    case states.PRE_BOUGHT: 
                        F.append(dp[m+1][states.BOUGHT_1] - prices[m])
                        F.append(dp[m+1][states.PRE_BOUGHT])
                    case states.BOUGHT_1:
                        F.append(dp[m+1][states.SOLD_1] + prices[m])
                        F.append(dp[m+1][states.BOUGHT_1])
                    case states.SOLD_1:  
                        F.append(dp[m+1][states.SOLD_1])
                        F.append(dp[m+1][states.BOUGHT_2] - prices[m])
                    case states.BOUGHT_2:
                        F.append(dp[m+1][states.BOUGHT_2])
                        F.append(dp[m+1][states.SOLD_2] + prices[m])
                    case states.SOLD_2:
                        F.append(dp[m+1][states.SOLD_2])

                dp[m][s_m] = max(F)

        return dp[0][states.PRE_BOUGHT]  