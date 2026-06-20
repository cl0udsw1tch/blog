class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        M=len(flights)

        X=defaultdict(list)
        for flight in flights:
            X[flight[0]].append(flight)

        memo={}
        for i in range(n):
            if i==dst: continue
            memo[(i, 0)]=float('inf')
        for remaining in range(k+1):
            memo[(dst, remaining)]=0
        def dfs(s):
            if s in memo: return
            i,remaining=s

            F=[float('inf')]
            for x,to,cost in X[i]:
                s_p=to,remaining-1
                dfs(s_p)
                f=cost+memo[s_p]
                F.append(f)
            f_min=min(F)
            memo[s]=f_min

        dfs((src,k+1))
        return memo[(src,k+1)] if not math.isinf(memo[(src,k+1)]) else -1

