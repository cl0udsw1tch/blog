class states:
    PRE_BOUGHT  =0
    BOUGHT      =1
    SOLD        =2
    COOL_DOWN   =3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        stage_m = 0...M-1 subproblem f*_m(s_m) solves the problem for [m...M-1]
        s_m: havent bought (0), bought (1), sold (2), cool-down (3) ...
        x_m: buying, selling, or nothing
        '''

        M= len(prices)
        dp = [[-float('inf')] * 4 for _ in range(M)]


        dp[M-1][states.PRE_BOUGHT]  = 0
        dp[M-1][states.BOUGHT]      = prices[M-1]
        dp[M-1][states.SOLD]        = 0
        dp[M-1][states.COOL_DOWN]   = 0

        for m in range(M-2, -1, -1):

            for s_m in [0,1,2,3]:

                F=[]
                match s_m:
                    case states.PRE_BOUGHT:
                        F.append(dp[m+1][states.PRE_BOUGHT])
                        F.append(dp[m+1][states.BOUGHT] - prices[m])
                    case states.BOUGHT:
                        F.append(dp[m+1][states.BOUGHT])
                        F.append(dp[m+1][states.SOLD] + prices[m])
                    case states.SOLD:
                        F.append(dp[m+1][states.SOLD])
                        F.append(dp[m+1][states.COOL_DOWN])
                    case states.COOL_DOWN:
                        F.append(dp[m+1][states.COOL_DOWN])
                        F.append(dp[m+1][states.BOUGHT] - prices[m])

                dp[m][s_m]=max(F)

        return dp[0][states.PRE_BOUGHT]