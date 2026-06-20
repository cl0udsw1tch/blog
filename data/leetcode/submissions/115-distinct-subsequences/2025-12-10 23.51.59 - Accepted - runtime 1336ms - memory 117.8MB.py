class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t)==1:
            return s.count(t)
        M=len(s)
        N=len(t)


        memo={}
        for n in range(N):
            memo[(M, n)] = 0
        for m in range(M+1):
            memo[(m, N)] = 1

        def dfs(r):
            if r in memo:
                return
            (m,n)=r
            F=[0,0]

            r_mp1=(m+1, n)
            dfs(r_mp1)
            F[0]=memo[r_mp1]

            if s[m]==t[n]:
                r_mp1=(m+1, n+1)
                dfs(r_mp1)
                F[1]=memo[r_mp1]
            
            f_sum=sum(F)
            memo[r]=f_sum


        dfs((0,0))
        return memo[(0,0)]
            