class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        M=len(nums)
        if M==1:
            if target in nums:
                return [0,0]
            return [-1,-1]

        
        P=lambda x: nums[x]<target
        l,r=-1,M
        while l+1<r:
            MID=(l+r)//2
            if P(MID):
                l=MID
            else:
                r=MID

        if r==M: return [-1,-1]
        if nums[r]!=target: return [-1,-1]

        start,l=r,r
        P=lambda x: nums[x]<target+1
        r=M
        while l+1<r:
            MID=(l+r)//2
            if P(MID):
                l=MID
            else:
                r=MID
        end=l
        return [start, end]

