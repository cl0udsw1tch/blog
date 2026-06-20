class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        M=len(nums)
        if M==0: return []
        if M==1:
            return [f"{nums[0]}"]
        
        r=[]
        l,prev=nums[0],nums[0]
        for m in range(1,M):
            num=nums[m]
            if num==prev+1:
                prev+=1
            else:
                r.append(f"{l}->{prev}" if prev>l else f"{l}")
                l,prev=num,num
        r.append(f"{l}->{prev}" if prev>l else f"{l}")
        return r
