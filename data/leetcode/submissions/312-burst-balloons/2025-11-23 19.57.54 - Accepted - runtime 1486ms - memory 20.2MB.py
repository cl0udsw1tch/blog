class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        stage_n: 0...n-1 subproblem f*_n(s_n) solves the problem for (n...s_n) exclusive
        s_n: right index of subset
        x_n: last balloon popped in (n...s_n) exclusive
        f_n(s_n, x_n) = f*_{n+1}(n,x_n) + n*x_n*s_n + f*_{n+1}(x_n, s_n)
        f*_n(s_n)=max_{x_n}(f_n(s_n))
        '''
        
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums)*max(nums)+max(nums)

        nums.append(1)
        nums.insert(0, 1)
        M=len(nums)
        N=M
        
        dp=[[0 for _ in range(N)] for _ in range(M)]

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            num_m=nums[m]
            for s_m in range(m+2, N):
                num_s_m=nums[s_m]
                F=[]
                for x_m in range(m+1, s_m):
                    F.append(dp[m][x_m] + num_m*nums[x_m]* num_s_m + dp[x_m][s_m])
                f_max=max(F)
                stage_m[s_m]=f_max
        return dp[0][-1]