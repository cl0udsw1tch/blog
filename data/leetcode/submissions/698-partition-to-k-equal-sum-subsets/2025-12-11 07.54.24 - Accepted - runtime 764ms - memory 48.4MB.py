class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        '''
        s: (mask, #subsets unfilled)

        '''
        M=len(nums)
        if M==1:
            return k==1
        total=sum(nums)
        if total % k: return False
        target=total//k

        memo={}
        def dfs(s):
            if s in memo:
                return
            
            mask, subset_total, sets_remaining = s
            if not sets_remaining:
                memo[s]=True
                return 
            F=[False for _ in range(M)]
            for x_m in range(M):
                bit = 1<<x_m
                if bit & mask: continue
                curr=subset_total + nums[x_m]
                if curr > target: continue

                subset_total_p=curr if curr < target else 0
                mask_p = mask | bit
                sets_remaining_p = sets_remaining if curr < target else sets_remaining-1

                s_p=(mask_p, subset_total_p, sets_remaining_p)
                dfs(s_p)
                f=memo[s_p]
                F[x_m]=f
                if f: break
            f_any=any(F)
            memo[s]=f_any

        dfs((0,0,k))
        return memo[(0,0,k)]


    
