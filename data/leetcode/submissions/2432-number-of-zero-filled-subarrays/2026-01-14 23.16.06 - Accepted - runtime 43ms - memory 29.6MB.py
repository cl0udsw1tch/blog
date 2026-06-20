class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return int(nums[0]==0)

        dp=[0]*(M+1)

        for m in range(M-1,-1,-1):
            if nums[m]==0:
                dp[m]=1+dp[m+1]

        return sum(dp)