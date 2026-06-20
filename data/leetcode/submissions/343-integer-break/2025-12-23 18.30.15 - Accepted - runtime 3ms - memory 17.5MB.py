class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n==2: return 1

        memo={}
        memo[(1,0)]=1
        memo[(2,1)]=1
        memo[(2,0)]=2

        def dfs(s):
            if s in memo: return
            m,o=s
            F=[] if o else [m]
            for x in range(1, m//2+1):
                l,r=x,m-x
                dfs((l,0))
                dfs((r,0))
                F.append(memo[(l,0)]*memo[(r,0)])
            f_max=max(F)
            memo[s]=f_max

        dfs((n,1))
        print(memo)
        return memo[(n,1)]
