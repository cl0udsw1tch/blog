class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        M=len(nums)
        if M<=2: return 0

        dp=[[0] for _ in range(M)]
        dp[-1][0]=(0,-float('inf'))

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            stage_m[0]=(stage_mp1[0][0]+1 if nums[m+1]-nums[m]==stage_mp1[0][1] else 0), nums[m+1]-nums[m]

        return sum([stage[0][0] for stage in dp])