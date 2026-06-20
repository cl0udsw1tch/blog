class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<=5: return n

        dp=[[(0,None)] for _ in range(n+1)]

        dp[1][0]=1, (0,0,0)
        dp[2][0]=2, (2,1,1)
        
        for m in range(3, n+1):
            stage_m=dp[m]
            stage_mm1=dp[m-1]
            s_m=0
            s_mm1=0
            next2, next3, next5=dp[m-1][s_mm1][1]
            f_min=min(2*dp[next2][0][0], 3*dp[next3][0][0], 5*dp[next5][0][0])
            f_min_next=(next2, next3, next5)
            if f_min==2*dp[next2][0][0]:
                f_min_next=(f_min_next[0]+1, f_min_next[1], f_min_next[2])
            if f_min==3*dp[next3][0][0]:
                f_min_next=(f_min_next[0], f_min_next[1]+1, f_min_next[2])
            if f_min==5*dp[next5][0][0]:
                f_min_next=(f_min_next[0], f_min_next[1], f_min_next[2]+1)

            stage_m[s_m]=f_min,f_min_next

        return dp[n][0][0]