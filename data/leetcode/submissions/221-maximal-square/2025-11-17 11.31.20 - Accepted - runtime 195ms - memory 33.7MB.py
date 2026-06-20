class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        stage_k:k=1..min(N, M) subproblem solves the problem for all grids of size k by k
        s_k: top-left coordinate of grid
        x_k: the subgrids with offsets (0,0) (0,1) (1,0) (1,1) and dimension k-1 x k-1 
        s_{k+1} = s_k + x_k
        f_k(s_k, x_k) = f_{k-1}(s_{k+1})
        f*_k(s_k) = all_{x_k}(f_{k-1}(s_{k+1}))
        '''

        M=len(matrix)
        N=len(matrix[0])
        intMat=[[int(c) for c in row] for row in matrix]
        if N==1 or M==1:
            return int(any([any(row) for row in intMat]))
        if not any([any(row) for row in intMat]):
            return 0

        K=min(N, M)
        
        dp=[[0 for _ in range(N)] for _ in range(M)]
        dp[-1]=intMat[-1]
        X=[(0,-1), (1,0), (1,-1)]
        
        for k in range(M-2,-1,-1):
  
            stage_k=dp[k]
            for s_k in range(N):
                if not intMat[k][s_k]:
                    stage_k[s_k]=0
                    continue
                F=[]
                for x_k in X:
                    f=dp[k+x_k[0]][s_k+x_k[1]] if s_k>0 else 0
                    F.append(f)
                f_min=1+min(F)
                stage_k[s_k]=f_min

        maxK=max([max(stage) for stage in dp])
        return maxK**2
