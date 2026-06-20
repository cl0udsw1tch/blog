class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        M=len(nums)
        if M==1: return 1

        ptr1,ptr2=0,0
        k=0
        while ptr1<M and ptr2<M:
            num1,num2=nums[ptr1],nums[ptr2]
            nums[k]=num1
            k+=1
            while num2==num1:
                ptr2+=1
                if ptr2==M: break
                num2=nums[ptr2]
            ptr1=ptr2

        return k