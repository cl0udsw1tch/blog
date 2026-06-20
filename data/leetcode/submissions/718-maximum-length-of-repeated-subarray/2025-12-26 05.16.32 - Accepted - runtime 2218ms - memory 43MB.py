class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M=len(nums1)
        N=len(nums2)

        if M==1:
            return int(nums1[0] in nums2)
        if N==1:
            return int(nums2[0] in nums1)

        dp=[[0 for _ in range(N+1)] for _ in range(M+1)]
        for m in range(M-1,-1,-1):
            for s_m in range(N-1,-1,-1):
                f=int(nums1[m]==nums2[s_m])
                if nums1[m]==nums2[s_m]:
                    f=max(f,1+dp[m+1][s_m+1])
                else:
                    f=0
                dp[m][s_m]=f
        return max([max(stage) for stage in dp])
