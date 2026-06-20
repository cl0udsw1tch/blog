class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        stage_n: n=0...N-1 subproblem f_n*(s_n) solves the problem for coins[n..N-1] and amount s_n
        s_n: amount
        x_n: feasible number of coin_n to use
         => s_{n+1} = s_n - x_n * coin_n >= 0
        f_n(s_n,x_n) = x_n + f*_{n+1}(s_{n+1}) 
        f*_n(s_n) = \sum(f*_{n+1}(s_n), f*_n(s_n - coin_n))

        '''

        if amount==0:
            return 1
        N=len(coins)
        if N==1:
            return int(amount % coins[0] == 0)

        dp = [[0 for _ in range(amount+1)], [0 for _ in range(amount+1)]]
        dp[1][0]=1
        for n in range(N-1, -1, -1):
            stage_n=dp[0]
            stage_np1=dp[1]
            coin_n=coins[n]
            for s_n in range(amount+1):
                f_sum=stage_np1[s_n] + ((stage_n[s_n-coin_n]) if s_n>=coin_n else 0)
                stage_n[s_n]=f_sum
            dp[1]=stage_n
            dp[0]=[0 for _ in range(amount+1)]
    
        r=dp[1][amount]
        return r
            




        