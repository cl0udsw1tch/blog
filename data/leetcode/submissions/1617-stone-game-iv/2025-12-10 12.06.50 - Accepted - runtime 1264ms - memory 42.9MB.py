class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        s: (remaining)
        '''

        if n==1: return True
        if n==2: return False
        if n==3: return True
        if n==4: return True

        memo=[None for _ in range(n+1)]
        memo[0]=False
        memo[1]=True
        def dfs(s):
            if memo[s] is not None:
                return
            for x in range(1, math.floor(math.sqrt(s))+1):
                s_p=s-x**2
                dfs(s_p)
                if not memo[s_p]:
                    memo[s]=True
                    return
            memo[s]=False
        dfs(n)
        return memo[n]
            
