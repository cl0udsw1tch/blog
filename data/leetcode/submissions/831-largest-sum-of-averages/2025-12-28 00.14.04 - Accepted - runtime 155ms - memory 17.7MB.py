class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        M=len(nums)
        if k==1:
            return sum(nums)/M
        pref_sum=[0]*(M+1)
        for i in range(M):
            pref_sum[i+1]=pref_sum[i]+nums[i]
        mean=lambda s,e: (pref_sum[e]-pref_sum[s])/(e-s)
        
        dp=[[-float('inf') for _ in range(M)] for _ in range(k)]
        m=k-1
        for s_m in range(M):
            dp[m][s_m]=mean(s_m,M)
        
        for m in range(k-2,-1,-1):
            for s_m in range(M-1):
                F=[-float('inf')]
                for x_m in range(s_m+1,M):
                    F.append(mean(s_m,x_m)+dp[m+1][x_m])
                f_max=max(F)
                dp[m][s_m]=f_max
        return dp[0][0]