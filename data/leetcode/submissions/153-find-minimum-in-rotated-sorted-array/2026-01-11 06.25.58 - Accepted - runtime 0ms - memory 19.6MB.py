class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        M=len(nums)
        if M==1: return nums[0]
        if nums[-1]>nums[0]<nums[1]: return nums[0]
        if nums[0]>nums[-1]<nums[-2]: return nums[-1]
        
        P=lambda l: (lambda x: nums[x]<nums[l])
        l,r=0,M-1
        while l+1<r:
            MID=(l+r)//2
            if P(l)(MID):
                r=MID
            else:
                l=MID
        return nums[r]