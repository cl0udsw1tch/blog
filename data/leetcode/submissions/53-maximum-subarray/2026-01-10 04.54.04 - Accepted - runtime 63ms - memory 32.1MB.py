class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1:
            return nums[0]

        dp=[None for _ in range(M)]

        dp[-1]=nums[-1]

        for m in range(M-2,-1,-1):
            dp[m]=max(nums[m],nums[m]+dp[m+1])
        return max([stage for stage in dp])