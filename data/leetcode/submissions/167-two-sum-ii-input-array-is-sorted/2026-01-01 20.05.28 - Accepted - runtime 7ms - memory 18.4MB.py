class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        M=len(numbers)
        if M==2:
            return [1,2]
        
        ptr1,ptr2=0,M-1
        while ptr1<ptr2:
            if numbers[ptr1]+numbers[ptr2]==target:
                return [ptr1+1, ptr2+1]
            if target-numbers[ptr1]>=numbers[ptr2]:
                ptr1+=1
            else:
                ptr2-=1