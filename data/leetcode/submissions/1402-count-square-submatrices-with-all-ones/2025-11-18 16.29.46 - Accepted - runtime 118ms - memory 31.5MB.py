import numpy as np
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        '''
        # stage_m: m=1...M-1 subproblem f*_m(s_m) finds the largest square with top-right corner (m, s_m)
        # s_m:  column index
        # x_m: for a given s_m, this corresponds to the offset of the left (0, -1) bottom (1, 0) and
        diagonal (1, -1) cells
        => s_{m+1} = s_m + x_m[1]
        => m'=m+x_m[0]
        # f_m(s_m, x_m) = f*_{m'}(s_{m+1}) gives the largest square with top-right corner (m',s_{m+1})
        # f*_m(s_m) = 1 + min_{x_m}(f_m(s_m, x_m)) if (m, s_m) == 1 else 0
        '''

        intMat=[[int(c) for c in row] for row in matrix]
        M, N = len(matrix) , len(matrix[0])
        if N==1 or M==1:
            return sum([sum(row) for row in intMat])

        dp=[[], intMat[-1]]
        X=[(0,-1), (1,0), (1,-1)]
        total = sum(dp[1])

        for m in range(M-2,-1,-1):
            stage_m=[0 for _ in range(N)]
            dp[0]=stage_m
            stage_mp1=dp[1]
            for s_m in range(N):
                if not intMat[m][s_m]:
                    stage_m[s_m]=0
                    continue
                F=[]
                for x_m in X:
                    s_mp1=s_m+x_m[1]
                    f=dp[x_m[0]][s_mp1] if (s_mp1 >= 0 and s_mp1 < N) else 0
                    F.append(f)
                f_min=1+min(F)
                stage_m[s_m]=f_min
                total+= f_min

            dp[1]=stage_m

        return total





            