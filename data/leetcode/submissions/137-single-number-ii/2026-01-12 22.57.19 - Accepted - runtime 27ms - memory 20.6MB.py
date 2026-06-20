class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        r=0
        for i in range(32):
            s=0
            for num in nums:
                s+=(num>>i) & 1
            s=s%3
            r=r | (s<<i)
        return r if r<(1<<31) else r-(1<<32)