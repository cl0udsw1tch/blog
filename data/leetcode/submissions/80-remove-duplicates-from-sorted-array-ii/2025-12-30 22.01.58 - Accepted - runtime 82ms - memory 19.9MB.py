class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        M=len(nums)
        if M<=2: return M

        ptr1,ptr2=0,0
        k=0

        while ptr1<M and ptr2<M:
            rem=2
            while nums[ptr1]==nums[ptr2]:
                if rem: 
                    rem-=1
                    nums[k]=nums[ptr1]
                    k+=1
                ptr2+=1
                if ptr2==M: break
            ptr1=ptr2
            
        return k