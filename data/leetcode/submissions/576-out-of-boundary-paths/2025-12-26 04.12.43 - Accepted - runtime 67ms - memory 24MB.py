class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        if maxMove==0: return 0
        MOD=10**9+7

        memo={}

        for movesRemaining in range(0,maxMove+1):
            for j in range(0,n):
                memo[(-1,j, movesRemaining)]=1
                memo[(m, j, movesRemaining)]=1
            for i in range(0,m):
                memo[(i, -1,movesRemaining)]=1
                memo[(i, n,movesRemaining)]=1

        for i in range(m):
            for j in range(n):
                memo[(i,j,0)]=0

        def dfs(s):
            if s in memo: return
            i,j, movesRemaining=s

            F=[]
            for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                i_p,j_p=i+x,j+y
                movesRemaining_p=movesRemaining-1
                s_p=i_p,j_p,movesRemaining_p
                dfs(s_p)
                F.append(memo[s_p])
            f_sum=sum(F)
            memo[s]=f_sum

        s=startRow,startColumn,maxMove
        dfs(s)
        return memo[s] % MOD

