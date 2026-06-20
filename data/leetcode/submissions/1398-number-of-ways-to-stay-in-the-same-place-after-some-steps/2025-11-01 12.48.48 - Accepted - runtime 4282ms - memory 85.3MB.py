class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        #stage n: number of steps from steps -> 1
        #state s_n: position/index
        #decisions x_n: go right, left, or stay. Importantly, the 
        #state transition function is x_{n+1} = g(s_n, x_n) = s_n + x_n 
        #where x_n = 1 if right, -1 if left, or 0 if stay

        #f(s_n, x_n): number of ways to arrive at 0 from s_n  after steps-n more 
        #steps given x_n is the immediate decision
        #f*(s_n) = \sum_{x_n} f(s_n, x_n) = total number of ways to get to 0 from s_n after all 
        #possible [3] immediate decisions 
        if arrLen == 1: return 1
        stage_N = 1
        dp = {
            1: {
                0: {"f": {0: 1}, "f*": 1},
                1: {"f": {-1: 1}, "f*": 1}
            }
        }
        for step in range(2, steps+1):
            stage_n = step
            dp[stage_n] = {}
            for prev_state in dp[stage_n - 1].keys():
                for x_i in [-1, 0, 1]:
                    s_n = prev_state - x_i
                    if s_n < 0 or s_n > arrLen - 1:
                        continue
                    if not s_n in list(dp[stage_n].keys()):
                        dp[stage_n][s_n] = {"f": {}, "f*": 0}

                    dp[stage_n][s_n]["f"][x_i] = dp[stage_n-1][prev_state]["f*"]
                    dp[stage_n][s_n]["f*"] += dp[stage_n][s_n]["f"][x_i] 

        sum = dp[steps][0]["f*"]
        return sum % (10**9 + 7)


        