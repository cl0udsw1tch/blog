class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        M=len(nums)
        if M==1: return nums[0]

        dp=[False for _ in range(M)]
        dp[0]=nums[0],0
        for m in range(1, M):
            dp[m]=max([(nums[m],m), (nums[m]+dp[m-1][0],dp[m-1][1])], key=lambda s: s[0])
        end, (MAX, start)=max(enumerate(dp), key=lambda s: s[1][0])

        pref_max=max(itertools.accumulate(nums[:start])) if start > 0 else 0
        suff_max=max(itertools.accumulate(nums[end+1:][::-1])) if end+1<M else 0

        r=max(MAX, pref_max+suff_max) if pref_max or suff_max else MAX

        for m in range(1, M):
            dp[m]=min([(nums[m],m), (nums[m]+dp[m-1][0],dp[m-1][1])], key=lambda s: s[0])
        end, (MIN, start)=min(enumerate(dp), key=lambda s: s[1][0])

        pref_max=max(itertools.accumulate(nums[:start])) if start > 0 else 0
        suff_max=max(itertools.accumulate(nums[end+1:][::-1])) if end+1<M else 0

        r=max(r, pref_max + suff_max) if pref_max or suff_max else r
        return r



