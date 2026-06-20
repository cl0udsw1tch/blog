class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m, t_m) solves the problem for piles m...s_m and pile count t_m
        s_m: right pile in interval
        t_m: number of piles to reduce to
        x_m: index to split [m,s_m] into two subintervals, one of which reduces to one
        f_m(s_m, t_m, x_m) = f*_m(x_m, 1) + f*_{x_m+1}(s_m, t_m-1) (t_m>=2)
        f*_m(s_m, t_m) = min_{x_m}{f_m(s_m, t_m, x_m)} (t_m>=2)
        f*_m(s_m, 1) = f*_m(s_m, k) + sum(stones[m...s_m])
        '''
        
        M=len(stones)
        if (M-k) % (k-1):
            return -1

        if M==1:
            return 0
        if M==2:
            if k!=2: return -1
            return sum(stones)
        if M==k:
            return sum(stones)
        
        N=M
        O=M+1
        dp=[[[math.inf for _ in range(O)] for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for s_m in range(m,N):
                dp[m][s_m][s_m-m+1]=0 #no cost
        for m in range(M-k+1):
            dp[m][m+k-1][1]=sum(stones[m:m+k])


        for m in range(M-2, -1, -1):
            for s_m in range(m+k,N):
                lenInterval=s_m-m+1
                for t_m in range(2,lenInterval+1):
                    if (lenInterval-t_m)%(k-1) != 0:
                        continue

                    F=[]
                    for x_m in range(m, s_m):
                        f=dp[m][x_m][1]+dp[x_m+1][s_m][t_m-1]
                        F.append(f)

                    dp[m][s_m][t_m]=min(F)

                t_m=1
                if (lenInterval - 1) % (k-1) == 0 :
                    dp[m][s_m][1] = dp[m][s_m][k] + sum(stones[m:s_m+1])

        return dp[0][-1][1]



        