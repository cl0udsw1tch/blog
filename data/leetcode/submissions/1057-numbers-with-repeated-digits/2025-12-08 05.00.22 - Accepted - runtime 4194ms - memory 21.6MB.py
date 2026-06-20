class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        # FINDING # OF UNIQUE, THEN SUBTRACT
        '''

        arr_n=list(map(int, str(n)))
        M=len(arr_n)
        dp=[[[0,0] for _ in range(1<<10)] for _ in range(M+1)]

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
                    F=[]
                    limit=arr_n[m] if t_m else 9
                    
                    for x_m in range(0, limit+1):
                        if ((1<<x_m) & s_m) > 0: continue
                        s_mp1=(1<<x_m) | s_m if (s_m != 0 or x_m !=0) else 0
                        t_mp1=int(t_m and (x_m==arr_n[m]))
                        F.append(stage_mp1[s_mp1][t_mp1])

                    stage_m[s_m][t_m]=sum(F)

        return n - (dp[0][0][1] - 1)
        '''
        # TRUE DIRECT DP
        '''
        s_m: mask
        t_m: tight
        u_m: at least 1 repeat
        f*_m(s_m, t_m, u_m)
        '''
        arr_n=list(map(int, str(n)))
        M=len(arr_n)
        dp=[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(1<<10)] for _ in range(M+1)]

        m=M
        stage_m=dp[m]
        for s_m in range(1<<10):
            for t_m in range(0,2):
                stage_m[s_m][t_m][0]=0
                stage_m[s_m][t_m][1]=1

        for m in range(M-1, -1, -1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            for s_m in range(1<<10):
                for t_m in range(2):
                    limit=arr_n[m] if t_m else 9
                    for u_m in range(2):
                        F=[]
                        for x_m in range(limit+1):
                            s_mp1=s_m | (1<<x_m) if (s_m or x_m) else 0
                            t_mp1=t_m & (x_m==limit) 
                            u_mp1=u_m | bool(s_m & (1<<x_m))
                            f=stage_mp1[s_mp1][t_mp1][u_mp1]
                            F.append(f)
                        f_sum=sum(F)
                        stage_m[s_m][t_m][u_m]=f_sum
        return dp[0][0][1][0]

                        





        