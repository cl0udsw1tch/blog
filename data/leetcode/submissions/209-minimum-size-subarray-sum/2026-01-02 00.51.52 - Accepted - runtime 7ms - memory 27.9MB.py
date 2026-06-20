class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return 1 if nums[0]>=target else 0
        if max(nums)>=target: return 1
        s=sum(nums)
        if s==target: return M
        if s<target: return 0

        ptr1,ptr2=0,0
        s=0
        r=M
        while ptr1<M and ptr2<M+1:
            if s<target:
                if ptr2==M: return r
                s+=nums[ptr2]
                ptr2+=1
                continue
            if s>=target:
                r=min(r, ptr2-ptr1)
                s-=nums[ptr1]
                ptr1+=1
        return r


