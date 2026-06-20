class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        M=len(nums)
        if M==1: return False
        if M==2: return nums[0]==nums[1] and k>0

        seen_dict={}
        for m in range(M):
            num=nums[m]
            if num in seen_dict and m-seen_dict[num]<=k: return True
            seen_dict[num]=m
        return False

