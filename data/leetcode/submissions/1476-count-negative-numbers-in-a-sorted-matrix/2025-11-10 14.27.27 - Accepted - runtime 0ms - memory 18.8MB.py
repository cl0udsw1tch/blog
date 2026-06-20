class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        stage_n: subproblem n = 0...N-1 is counting the negative numbers in grid[n:N]
        s_n: index of the first negative number in grid[n]
        x_n: index of the first negative number in grid[n+1]
            = s_{n+1}
        f_n(s_n,x_n) = (len(row)-s_n) + f*_{n+1}(s_{n+1})
        f*_n(s_n) = f_n(s_n, x_n)

        '''

        dp=[[-1],[-1]]
        R=len(grid)
        C=len(grid[0])

        s_n=-1
        for i in range(C):
            if grid[-1][i]<0:
                s_n=i
                break
        dp[1][0]=(s_n, (C-s_n) if s_n!=-1 else 0)
        for n in range(R-2, -1,-1):
            stage_n=dp[0]
            stage_np1=dp[1]
            s_n=-1
            s_np1,c=stage_np1[0]
            for i in range(s_np1, C):
                if grid[n][i]<0:
                    s_n=i
                    break
            f_max=((C-s_n) if s_n!=-1 else 0)+c
            stage_n[0]=(s_n, f_max)
            dp[1]=stage_n
            dp[0]=[-1]
        return dp[1][0][1]
            
            

        