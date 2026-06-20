class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) gives the score difference alice-bob for all optimal decisions
        taken when the last M-m piles are remaining, and M is set to s_m
        s_m: the value of M
        x_m: 1...2M = the number of piles the current player chooses
            => s_{m+1} = m+max(s_m, x_m)
        f_m(s_m, x_m) = sum(piles[m:m+x_m]) - f*_{m+x_m}(s_mp1)
        f*_m(s_m) = max_{x_m}(f_m(s_m, x_m))


        '''
        M=len(piles)
        if M==1: return piles[0]
        if M==2: return piles[0] + piles[1]
        if M==3: return piles[0] + piles[1]

        dp=[[0 for _ in range(M+1)] for _ in range(M+1)]

        m=M
        stage_m=dp[m]
        for s_m in range(1,M+1):
            stage_m[s_m]=0
        
        for m in range(M-1,-1,-1):
            stage_m=dp[m]
            for s_m in range(1,M+1):
                F=[-float("inf")]
                for x_m in range(1, 2*s_m + 1):
                    terminal=m+x_m-1
                    if terminal > M-1: break
                    s_mp1=max(s_m, x_m)
                    f=sum(piles[m:m+x_m]) - dp[m+x_m][s_mp1]
                    F.append(f)
                f_max=max(F)
                stage_m[s_m]=f_max
        return (sum(piles) + dp[0][1]) // 2

        