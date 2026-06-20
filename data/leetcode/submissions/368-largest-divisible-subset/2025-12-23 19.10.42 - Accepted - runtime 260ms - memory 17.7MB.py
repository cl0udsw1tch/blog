class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        M=len(nums)
        if M==1: return nums

        nums.sort()
        dp=[[None] for _ in range(M)]
        dp[-1][0]=(M-1,)
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            s_m=0
            s_mp1=0
            num_m=nums[m]
            F=[(m,)]
            for x_m in range(m+1, M):
                f_mp1=dp[x_m][s_mp1]
                num_mp1=nums[x_m]
                if num_mp1 % num_m == 0:
                    F.append((m,)+f_mp1)
            f_max=max(F, key = lambda f: len(f))
            stage_m[s_m]=f_max

        return [nums[i] for i in max(dp, key=lambda stage: len(stage[0]))[0]]
