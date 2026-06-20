class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        N = len(grid)
        if N == 1:
            return grid[0][0]

        if N == 2:
            return min([grid[0][0] + grid[1][1], grid[1][0] + grid[0][1]])

        dp = [[], grid[-1]]

        for n in range(N-2,-1,-1):
            stage_n=dp[0]
            stage_np1=dp[1]
            for idx in range(N):
                s_n = grid[n][idx]
                f = []
                for x_n in range(N):
                    if x_n==idx:
                        continue
                    s_np1=stage_np1[x_n]
                    f.append(s_n+s_np1)
                f_star=min(f)
                stage_n.append(f_star)
            dp[1]=stage_n
            dp[0]=[]

        return min(dp[1])
        
                
