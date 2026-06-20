class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1:
            return nums[0]
        
        dp=[[float('inf'), -float('inf')] for _ in range(M)] #smallest, largest
        dp[-1]=[nums[-1],nums[-1]]
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]

            F=[nums[m], nums[m] * stage_mp1[0], nums[m] * stage_mp1[1]]
            f_min,f_max=min(F),max(F)
            stage_m[0]=f_min
            stage_m[1]=f_max

        return max([stage[1] for stage in dp])

            