class Solution:
    def fib(self, n: int) -> int:
        
        if n==0: return 0
        if n==1: return 1

        memo={}
        memo[0]=0
        memo[1]=1

        def dfs(s):
            if s in memo: return

            dfs(s-1)
            dfs(s-2)
            memo[s]=memo[s-1]+memo[s-2]

        dfs(n)
        return memo[n]