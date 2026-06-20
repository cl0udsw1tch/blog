class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        M=numRows
        if M==1:
            return [[1]]
        if M==2:
            return [[1], [1,1]]


        dp=[[[]] for _ in range(M)]

        dp[0]=[[1]]

        for m in range(1,M):
            stage_m=dp[m]
            stage_mm1=dp[m-1]
            s_mm1=0
            s_m=0
            F=[1]
            for x_mm1 in range(1,m):
                F.append(stage_mm1[s_mm1][x_mm1]+stage_mm1[s_mm1][x_mm1-1])
            F.append(1)
            stage_m[s_m]=F
            
        return [stage_m[0] for stage_m in dp]

