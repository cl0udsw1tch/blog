class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        M=len(nums)
        if M==1:
            return True
        if M==2:
            return nums[0]>0

        dp=[[False] for _ in range(M)]
        dp[-1][0]=True

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            s_m=0
            if m+nums[m]>=M-1:
                stage_m[s_m]=True
                continue
            F=False
            for x_m in range(min(M-m-1,nums[m]),0,-1):
                f=dp[m+x_m][0]
                F=F or f
                if F: break
            stage_m[s_m]=F
        return dp[0][0]
