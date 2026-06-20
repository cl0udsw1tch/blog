class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        if n==1: return 1

        N=len(primes)
        dp=[[None] for _ in range(n+1)]

        dp[1][0]=1, tuple([1 for _ in range(N)])

        for m in range(2, n+1):
            stage_m=dp[m]
            stage_mm1=dp[m-1]
            s_m=0
            s_mm1=0

            f_mm1, g_mm1 = stage_mm1[s_mm1]
            f_m=float('inf')
            for x in range(N):
                f=primes[x]*dp[g_mm1[x]][s_mm1][0]
                f_m=min(f_m, f)
            g_m=()
            for x in range(N):
                g_m+=(g_mm1[x]+1 if f_m==primes[x]*dp[g_mm1[x]][s_mm1][0] else g_mm1[x],)
            stage_m[s_m]=f_m,g_m

        return dp[n][0][0]

