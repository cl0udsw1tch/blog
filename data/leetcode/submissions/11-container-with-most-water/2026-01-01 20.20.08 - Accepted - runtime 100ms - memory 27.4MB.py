class Solution:
    def maxArea(self, height: List[int]) -> int:
        M=len(height)
        if M==2:
            return min(height)

        ptr1,ptr2=0,M-1
        MAX=0
        while ptr1<ptr2:
            MAX=max(MAX, min(height[ptr1], height[ptr2])*(ptr2-ptr1))
            if height[ptr1]<height[ptr2]:
                ptr1+=1
            else:
                ptr2-=1
        return MAX