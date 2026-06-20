class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        stage_n: n=0...N-1 subproblem f_n*(s_n) solves the problem for coins[n...N-1] and s_n amount
        s_n: amount
        x_n: some number of coin_n [0...X_n] that is feasible (i.e X_n * coin_n <= s_n)
            => s_{n+1} = s_n - x_n * coin_n
        f_n(s_n, x_n) = x_n + f*_{n+1}(s_{n+1})
                      =
        f*_n(s_n) = \min_{x_n} (f_n(s_n, x_n))
                  = \min (f_n(s_n, 0)....f_n(s_n, X_n))
                  = \min (f*_{n+1}(s_n), f*_{n+1}(s_n-1 * coin_n) +1 ,..., f*_{n+1}(s_n- X_n * coin_n) + X_n)
                  = \min (f*_{n+1}(s_n), [ f*_{n+1}((s_n - coin_n)) + 1 ] , [ f*_{n+1}((s_n - coin_n) - coin_n ) + 1 ] + 1
                  ,..., 
                  [ f*_{n+1}((s_n-coin_n) - (X_n-1)* coin_n ) +  1] + (X_n-1))
                  = \min (f*_{n+1}(s_n), \min_{x_n = 0...X_n-1}(f*_n(s_n - x_n *coin_n) + x_n))
                  = \min (f*_{n+1}(s_n), f*_n(s_n - coin_n) + 1)

        '''

        if amount==0:
            return 0
        N=len(coins)
        if N==1:
            return amount // coins[0] if amount % coins[0] == 0 else -1

        dp = [[math.inf for _ in range(amount+1)], [math.inf for _ in range(amount+1)]]
        dp[1][0]=0
        for n in range(N-1, -1, -1):
            stage_n=dp[0]
            stage_np1=dp[1]
            coin_n=coins[n]
            for s_n in range(amount+1):
                f_star=min(stage_np1[s_n], (stage_n[s_n-coin_n]+1) if s_n>=coin_n else math.inf)
                stage_n[s_n]=f_star
            dp[1]=stage_n
            dp[0]=[math.inf for _ in range(amount+1)]
    
        r=dp[1][amount] if dp[1][amount] != math.inf else -1
        return r
            



