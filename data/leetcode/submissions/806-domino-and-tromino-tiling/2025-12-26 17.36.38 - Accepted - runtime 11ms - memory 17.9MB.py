class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1

        MOD=10**9+7

        NONE, TOP, BOTTOM=0,1,2
        
        dp=[[0,0,0] for _ in range(n+1)]
        dp[-1][NONE]=1
        dp[-1][TOP]=0
        dp[-1][BOTTOM]=0

        dp[-2][NONE]=1
        dp[-2][TOP]=0
        dp[-2][BOTTOM]=0

        for m in range(n-2,-1,-1):
            for s_m in [NONE, TOP, BOTTOM]:
                F=[]
                if s_m==NONE:

                    f=dp[m+1][NONE] #vertical domino
                    F.append(f)

                    f=dp[m+1][BOTTOM]
                    F.append(f)

                    f=dp[m+1][TOP]
                    F.append(f)
                
                    f=dp[m+2][NONE]
                    F.append(f)
                elif s_m==TOP:
                    f=dp[m+2][NONE]
                    F.append(f)

                    f=dp[m+1][BOTTOM]
                    F.append(f)
                elif s_m==BOTTOM:
                    f=dp[m+2][NONE]
                    F.append(f)

                    f=dp[m+1][TOP]
                    F.append(f)
                f_sum=sum(F)
                dp[m][s_m]=f_sum
        
        return dp[0][NONE] % MOD
