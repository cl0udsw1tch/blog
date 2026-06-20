class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        M=len(nums)
        if M==3:
            return [nums] if sum(nums)==0 else []

        nums.sort()
        index={v:i for i,v in enumerate(nums)}
        ptr1,ptr2=0,1
        r=[]
        while ptr1<M-2:
            if ptr1>0 and nums[ptr1]==nums[ptr1-1]:
                ptr1+=1
                continue
            ptr2=ptr1+1
            while ptr2<M-1:
                if ptr2>ptr1+1 and nums[ptr2]==nums[ptr2-1]:
                    ptr2+=1
                    continue
                s=nums[ptr1]+nums[ptr2]
                if -s in index and index[-s]>ptr2:
                    r.append([nums[ptr1], nums[ptr2], -s])
                ptr2+=1
            ptr1+=1
        return r
                