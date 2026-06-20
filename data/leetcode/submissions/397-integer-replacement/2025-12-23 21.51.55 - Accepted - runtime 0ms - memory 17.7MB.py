class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1: return 0

        memo={}
        memo[1]=0

        def dfs(s):
            if s in memo: return

            if s%2:
                dfs(s+1)
                dfs(s-1)
                memo[s]=1+min(memo[s+1],memo[s-1])
            else:
                dfs(s//2)
                memo[s]=1+memo[s//2]
        dfs(n)
        return memo[n]