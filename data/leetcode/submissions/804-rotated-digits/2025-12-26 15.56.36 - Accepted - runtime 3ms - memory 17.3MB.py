class Solution:
    def rotatedDigits(self, n: int) -> int:
        if n==1: return 0
        arr=list(map(int, str(n)))
        M=len(arr)
        NOT_TIGHT,TIGHT=0,1
        NOT_GOOD,GOOD=0,1

        dp=[[[(), ()] for _ in range(2)] for _ in range(M+1)]
        dp[-1][GOOD][NOT_TIGHT]=(0,1)
        dp[-1][GOOD][TIGHT]=(0,1)
        dp[-1][NOT_GOOD][NOT_TIGHT]=(0,0)
        dp[-1][NOT_GOOD][TIGHT]=(0,0)

        valid=[0,1,2,5,6,8,9]
        good=[2,5,6,9]

        for m in range(M-1,-1,-1):
            for s_m in [NOT_GOOD,GOOD]:
                for t_m in [NOT_TIGHT,TIGHT]:
                    F=[]
                    limit=9 if not t_m else arr[m]
                    for x in range(limit+1):
                        if x not in valid: continue
                        t_mp1=int(t_m and x == limit)
                        s_mp1=int(s_m or x in good) 
                        if s_m==NOT_GOOD:
                            f1=dp[m+1][s_mp1][t_mp1][NOT_GOOD]
                            f2=dp[m+1][s_mp1][t_mp1][GOOD]
                            F.append((f1,f2))
                        elif s_m==GOOD:
                            f1=0
                            f2=sum(dp[m+1][s_mp1][t_mp1]) 
                            F.append((f1,f2))
                    f_sum=(sum([f[0] for f in F]), sum([f[1] for f in F]))
                    dp[m][s_m][t_m]=f_sum

        return dp[0][NOT_GOOD][TIGHT][GOOD]
