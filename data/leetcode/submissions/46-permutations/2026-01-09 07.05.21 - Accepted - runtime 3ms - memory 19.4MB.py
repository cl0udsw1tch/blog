class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        M=len(nums)
        if M==1: return [nums]

        def backtrack(i, curr):
            if i==M: return [curr[:]]

            r=[]
            for num in nums:
                if num in curr: continue
                curr.append(num)
                r.extend(backtrack(i+1, curr))
                curr.pop()
            return r
        return backtrack(0, [])