class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        M=rowIndex
        if M==0:
            return [1]
        
        dp = [[[1]], [[]]]

        for m in range(1, M+1):
            stage_mm1=dp[0]
            stage_m=dp[1]

            s_mm1=0
            s_m=0

            F=[1]
            for x_mm1 in range(1, m):
                F.append(stage_mm1[s_mm1][x_mm1]+stage_mm1[s_mm1][x_mm1-1])
            F.append(1)
            stage_m[s_m]=F

            dp[0]=stage_m
            dp[1]=[[]]

        return dp[-2][0]
        
