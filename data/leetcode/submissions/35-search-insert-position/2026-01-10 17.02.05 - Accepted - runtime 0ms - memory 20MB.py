class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # invariant: P(l) AND NOT P(r)
        N=len(nums)
        l,r=-1,N
        P=lambda x: nums[x]<target
        while r>l+1:
            MID=(l+r)//2
            if P(MID):
                l=MID
            else:
                r=MID
        return r