class Solution:
    def search(self, nums: List[int], target: int) -> int:
        M=len(nums)
        if M==1: return -1*(nums[0]!=target)

        max_idx=None
        if nums[-1]<nums[0]>nums[1]: max_idx=0
        if nums[-2]<nums[-1]>nums[0]: max_idx=M-1

        if max_idx is None:
            max_idx=find_max(nums)
        if max_idx!=M-1:
            nums=nums[max_idx+1:] + nums[:max_idx+1]
        r = find_target(nums, target)
        return (r+max_idx+1) % M if r!=-1 else -1

def find_max(nums):
    M=len(nums)
    P=lambda l: (lambda x: nums[x]<nums[l]) # 2D predicate !!! Monotone still for fixed l
    l,r=0,M-1
    while r>l+1:
        MID=(l+r)//2
        if P(l)(MID):
            r=MID
        else:
            l=MID
    return l

def find_target(nums, target):
    M=len(nums)
    P=lambda x: nums[x]<target

    l,r=-1,M
    while r>l+1:
        MID=(l+r)//2
        if P(MID):
            l=MID
        else:
            r=MID
    return r if r<M and nums[r]==target else -1