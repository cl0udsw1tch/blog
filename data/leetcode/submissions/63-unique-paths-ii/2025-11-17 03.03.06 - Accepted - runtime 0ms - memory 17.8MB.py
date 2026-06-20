class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        stage_k: k=0...m-1 subproblem f*_k(s_n) solves the problem where grid[k][s_m] is the start point 
        s_n: column index
        x_n: moving right (0, 1) or down (1, 0)
         => s_{n+1} = s_n + x_n[0]
        f_n(s_n, x_n) = f*_n(s_{n+1}) if x=(0,1) and is feasible
                      = f*_{n+1}(s_{n+1}) if x=(1,0) and is feasible
        f*_n(s_n) = f*_n(s_{n+1}) + f*_{n+1}(s_{n+1})
    
        '''
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==1 or n==1:
            return int(not any([any(row) for row in obstacleGrid]))
        if obstacleGrid[-1][-1]:
            return 0
        
        dp=[[0 for _ in range(n)], [0 for _ in range(n)]]
        dp[1][-1]=1
        for s_k in range(n-2, -1, -1):
            if obstacleGrid[-1][s_k]:
                dp[1][0:s_k+1]=[0 for _ in range(s_k+1)]
                break
            dp[1][s_k]=1

        for k in range(m-2,-1,-1):
            stage_k=dp[0]
            stage_kp1=dp[1]

            for s_k in range(n-1, -1, -1):
                if obstacleGrid[k][s_k]:
                    stage_k[s_k]=0
                    continue
                F=[]
                for x_k in [(0,1),(1,0)]:
                    s_kp1=s_k+x_k[1]
                    kp1=k+x_k[0]
                    F.append(dp[kp1-k][s_kp1] if (kp1<m and s_kp1<n ) else 0)
                f_sum=sum(F)
                stage_k[s_k]=f_sum

            dp[1]=stage_k
            dp[0]=[0 for _ in range(n)]

        return dp[1][0]