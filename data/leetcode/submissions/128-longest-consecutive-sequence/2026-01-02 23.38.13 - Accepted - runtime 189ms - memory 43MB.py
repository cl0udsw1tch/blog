class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        M=len(nums)
        if M==0: return 0
        if M==1: return 1

        top_map,bottom_map={},{}
        r=1
        for m in range(M):
            num=nums[m]
            if num in top_map or num in bottom_map: continue
            top,bottom=num,num
            top_map[num],bottom_map[num]=1,1
            if num-1 in top_map:
                bottom=num-top_map[num-1]
                top_map[num]=top_map[num-1]+1
            if num+1 in bottom_map:
                top=num+bottom_map[num+1]
                bottom_map[num]=bottom_map[num+1]+1
            
            top_map[top]=top-bottom+1
            bottom_map[bottom]=top-bottom+1
            r=max(r, top-bottom+1)
        return r