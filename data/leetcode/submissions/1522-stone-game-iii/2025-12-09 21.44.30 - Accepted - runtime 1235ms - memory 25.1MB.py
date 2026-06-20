class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        M=len(stoneValue)
        if M==1:
            if stoneValue[0]==0: return "Tie"
            elif stoneValue[0] > 0: return "Alice"
            else: return "Bob"
        
        dp = [[0] for _ in range(M+1)]
        m=M
        stage_m=dp[m]
        s_m=0
        stage_m[s_m]=0

        for m in range(M-1,-1,-1):
            stage_m=dp[m]
            s_m=0
            F=[]
            for x_m in range(1,4):
                terminal=m+x_m-1
                if terminal>M-1: break
                s_mp1=0
                f=sum(stoneValue[m:m+x_m]) - dp[m+x_m][s_mp1]
                F.append(f)
            f_max=max(F)
            stage_m[s_m]=f_max
        
        delta=dp[0][0]
        if delta>0:
            return "Alice"
        elif delta<0: return "Bob"
        else: return "Tie"

