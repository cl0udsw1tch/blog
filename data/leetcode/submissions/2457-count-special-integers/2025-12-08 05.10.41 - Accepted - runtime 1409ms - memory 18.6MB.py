class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        
        arr_n=list(map(int, str(n)))
        M=len(arr_n)

        if n<=10:
            return n

        dp=[[[0 for _ in range(2)] for _ in range(1<<10)] for _ in range(M+1)]
        m=M
        stage_m=dp[m]
        for s_m in range(1<<10):
            stage_m[s_m][0]=1
            stage_m[s_m][1]=1
        
        for m in range(M-1,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            for s_m in range(1<<10):
                for t_m in range(2):
                    limit=arr_n[m] if t_m else 9
                    F=[]
                    for x_m in range(limit+1):
                        if s_m & (1<<x_m): continue
                        s_mp1=s_m | (1<<x_m) if (s_m or x_m) else 0
                        t_mp1=t_m and (x_m == limit)
                        f=stage_mp1[s_mp1][t_mp1]
                        F.append(f)
                    f_sum=sum(F)
                    stage_m[s_m][t_m]=f_sum
        return dp[0][0][1] - 1