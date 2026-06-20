class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        stage_k: k=0..M-1 subproblem f*_k(s_k) solves the problem the largest rectangle who's top right corner
        is cell (k, s_k)
        s_k=column index
        x_k = all cells to the left and including (k, s_k)
        =>s_{k+1} = s_k + x_k
        f_k(s_k, x_k) = 0 if empty else height of column below and including cell at (k, x_k) = 1+f_{k+1}(s_{k+1})[1]
        f*_k(s_k) = largest rectangle in union of x_k columns and matrix[k][s_k]

        M=len(matrix)
        N=len(matrix[0])
        intMat=[[int(c) for c in row] for row in matrix]
        if not any([any(row) for row in intMat]):
            return 0

        dp=[[(0,0) for _ in range(N)] for _ in range(M+1)]

        for k in range(M-1, -1, -1):
            stage_k=dp[k]
            for s_k in range(N):
                if not intMat[k][s_k]:
                    stage_k[s_k]=(0,0)
                    continue
                if s_k==0:
                    stage_k[s_k] = (1+dp[k+1][0][1], 1+dp[k+1][0][1])
                    continue
                F=[0 for _ in range(s_k+1)]
                minHeight=math.inf
                for x_k in range(s_k, -1,-1):
                    if intMat[k][x_k]==0:
                        break
                    minHeight=min(minHeight, 1+dp[k+1][x_k][1])
                    F[x_k] = minHeight*(s_k-x_k+1)

                f_max=max(F)
                stage_k[s_k]=(f_max, 1+dp[k+1][s_k][1])

        maxR=max([max([s[0] for s in stage]) for stage in dp])
        return maxR

        '''

        M=len(matrix)
        N=len(matrix[0])
        intMat=[[int(c) for c in row] for row in matrix]
        if not any([any(row) for row in intMat]):
            return 0

        heights=[0 for _ in range(N)]
        maxArea=0

        for m in range(M-1,-1,-1):
            for n in range(N):
                heights[n]= (heights[n]+1) if intMat[m][n] else 0
            
            idxs=[]

            for n in range(N):
                height_n=heights[n]
                if not idxs:
                    idxs.append(n)
                    continue
                rightIdx=n-1
                while idxs and height_n < heights[idxs[-1]]:
                    leftIdx=idxs[-2]+1 if len(idxs) > 1 else 0
                    width=rightIdx-leftIdx+1
                    height=heights[idxs[-1]]
                    maxArea=max(maxArea, height * width)
                    idxs.pop()
                idxs.append(n)
            rightIdx=N-1
            while idxs:
                leftIdx=idxs[-2]+1 if len(idxs)>1 else 0
                width=rightIdx-leftIdx+1
                height=heights[idxs[-1]]
                maxArea=max(maxArea, height*width)
                idxs.pop()
        return maxArea



        
        