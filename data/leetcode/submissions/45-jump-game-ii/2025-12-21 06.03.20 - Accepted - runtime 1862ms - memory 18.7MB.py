class Solution:
    def jump(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1:
            return 0
        
        dp=[[0] for _ in range(M)]
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            s_m=0
            F=[float('inf')]*(nums[m]+1)
            for x_m in range(1,min(nums[m]+1, M-m)):
                f=1+dp[m+x_m][0]
                F[x_m]=f
            f_min=min(F)
            stage_m[s_m]=f_min
        return dp[0][0]