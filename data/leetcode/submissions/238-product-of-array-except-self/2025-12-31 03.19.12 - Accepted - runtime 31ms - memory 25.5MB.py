class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        M=len(nums)
        if M==2: return [nums[1], nums[0]]
        pref_prod, suff_prod=[0]*M, [0]*M
        pref_prod[0]=nums[0]
        for m in range(1, M):
            pref_prod[m]=nums[m]*pref_prod[m-1]
        suff_prod[-1]=nums[-1]
        for m in range(M-2,-1,-1):
            suff_prod[m]=nums[m]*suff_prod[m+1]

        r=[0]*M
        r[0]=suff_prod[1]
        r[-1]=pref_prod[-2]
        for m in range(1,M-1):
            r[m]=pref_prod[m-1]*suff_prod[m+1]

        return r

