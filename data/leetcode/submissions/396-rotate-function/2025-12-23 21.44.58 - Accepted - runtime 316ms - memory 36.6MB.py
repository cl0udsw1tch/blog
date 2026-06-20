class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return 0

        s=sum(nums)

        dp=[[0] for _ in range(M)]
        dp[0][0]=sum([i * nums[i] for i in range(M)])

        for m in range(1, M):
            stage_m=dp[m]
            stage_mm1=dp[m-1]
            s_m, s_mm1=0,0

            f_mm1=stage_mm1[s_mm1]
            f=f_mm1
            f+=s
            f-=M*nums[-m]

            stage_m[s_m]=f
        return max(dp, key=lambda stage: stage[0])[0]

