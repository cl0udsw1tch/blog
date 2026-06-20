class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        M=len(nums)
        if M<=2: return nums[0]

        freq=defaultdict(int)
        r=(-1,-float('inf'))
        for num in nums:
            freq[num]+=1
            if freq[num]>r[1]:
                r=(num, freq[num])
            if freq[num]>(M>>1): break 
        return r[0]