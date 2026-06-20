class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for matrix[m...M-1] starting at (m, s_m)
        s_m: col index
        x_n: down, down-left, down-right 0, -1, 1
        => s_{m+1} = s_m + x_m[1]
        f_m(s_m, x_m) = matrix[m][s_m] + f*_{m+1}(s_{m+1}) 
        f*_m(s_m) = max_{x_m}(f_m(s_m, x_m))

        '''

        M=len(matrix)
        N=len(matrix[0])
        if N==1:
            return sum([row[0] for row in matrix])
        if M==1:
            return max([row[0] for row in matrix])

        dp=[[], [0 for _ in range(N)]]
        dp[1] = matrix[-1]

        X=[0,-1, 1]

        for m in range(M-2, -1, -1):
            stage_m=[0 for _ in range(N)]
            stage_mp1=dp[1]
            
            for s_m in range(N):
                F=[]
                s_m_num=matrix[m][s_m]
                for x_m in X:
                    s_mp1=s_m+x_m
                    f=(s_m_num+stage_mp1[s_mp1]) if (s_mp1>=0 and s_mp1<N) else math.inf
                    F.append(f)
                f_min=min(F)
                stage_m[s_m]=f_min
            dp[1]=stage_m

        return min(dp[1])
        