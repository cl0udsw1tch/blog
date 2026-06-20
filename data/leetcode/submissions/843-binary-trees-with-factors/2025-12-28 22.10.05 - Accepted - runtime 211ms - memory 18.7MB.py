class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        MOD=10**9+7
        arr.sort()
        M=len(arr)
        if M==1: return 1

        prod=[[] for _ in range(M)]
        index = {v: i for i, v in enumerate(arr)}

        for m in range(M):
            for x in range(m):
                if arr[m] % arr[x] != 0:
                    continue
                y = int(arr[m] / arr[x])
                if y in index:
                    prod[m].append((x, index[y]))
        memo=[None]*M
        memo[0]=1
        self.t=1
        def dfs(s):
            if memo[s] is not None: return
            F=1
            for x,y in prod[s]:
                dfs(x)
                dfs(y)
                F+=memo[x]*memo[y]
            memo[s]=F
            self.t+=F
        
        for m in range(M):
            dfs(m)
        return self.t % MOD
