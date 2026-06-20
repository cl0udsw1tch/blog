class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return nums[0]
        nums.sort(reverse=True)
        groups=defaultdict(int)
        for m in range(M):
            groups[nums[m]]+=1
        memo={}
        memo[M]=0
        memo[M-1]=nums[M-1]

        def dfs(s):
            if s in memo: return
            F=[]
            s_p=s+groups[nums[s]]
            if s_p<M and nums[s_p]==nums[s]-1:
                s_p+=groups[nums[s_p]]
            dfs(s_p)
            f=nums[s]*groups[nums[s]]+memo[s_p]
            F.append(f)

            s_p=s+groups[nums[s]]
            dfs(s_p)
            f=memo[s_p]
            F.append(f)

            f_max=max(F)
            memo[s]=f_max

        dfs(0)
        return memo[0]



        


