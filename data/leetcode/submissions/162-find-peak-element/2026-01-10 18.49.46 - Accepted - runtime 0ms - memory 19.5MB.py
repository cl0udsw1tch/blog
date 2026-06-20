class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return 0
        if nums[0]>nums[1]: return 0
        if nums[-1]>nums[-2]: return M-1

        peak=lambda x: nums[x-1]<nums[x]>nums[x+1]
        P=lambda x: nums[x]>nums[x-1]

        l,r=0,M-1
        while r>l+1:
            MID=(l+r)//2

            if peak(MID):
                return MID

            if P(MID):
                l=MID
            else:
                r=MID
        return r