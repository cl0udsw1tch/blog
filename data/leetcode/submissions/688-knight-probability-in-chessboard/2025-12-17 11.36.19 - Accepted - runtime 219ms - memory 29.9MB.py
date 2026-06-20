class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k==0:
            return float(row>-1 and row<n and column>-1 and column<n)
        
        X=[(2,1),(-2,1),(2,-1), (-2,-1)]
        X.extend([(move[1],move[0]) for move in X])
        memo={}

        def dfs(s):
            if s in memo: return
            
            m, (i, j) = s
            if not ((i>-1 and i<n) and (j>-1 and j<n)):
                memo[s]=0
                return
            if m==k: 
                memo[s]=float((i>-1 and i<n) and (j>-1 and j<n))
                return
            

            F=[0]*8
            c=0
            for x in X:
                pos_mp1=(i+x[0], j+x[1])
                mp1=m+1
                s_mp1=(mp1, pos_mp1)
                dfs(s_mp1)
                F[c]=(1/8)*memo[s_mp1]
                c+=1
            memo[s]=sum(F)

        dfs((0,(row, column)))
        return memo[(0, (row, column))]


