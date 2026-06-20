class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''

        '''

        M=len(piles)
        if M<=2: return True
        if M==3: return piles[0]+piles[2] > piles[1]

        dp=[[0 for _ in range(M)] for _ in range(M)]
        m=M-1
        stage_m=dp[m]
        sz=1
        for s_m in range(M):
            stage_m[s_m]=piles[s_m]

        for m in range(M-2, -1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            sz=M-m
            for s_m in range(M):
                terminal=s_m+sz-1
                if terminal > M-1: continue
                F=[]
                for x_m in [s_m, terminal]:
                    s_mp1=s_m if x_m==terminal else s_m+1
                    f=piles[x_m]-stage_mp1[s_mp1]
                    F.append(f)
                f_max=max(F)
                stage_m[s_m]=f_max
        return dp[0][0] > 0