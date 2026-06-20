class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ''' 
        stage_n: n=0...N-1 subproblem solves the problem for nums[n...N] and each possible sum s<=Target
        s_n: 0...Target
        x_n: adding or subtracting the current in nums[n]
            => adding:      x_n = -nums[n] => s_{n+1}=s_n - nums[n]
            => subtracting: x_n = +nums[n] => s_{n+1}=s_n + nums[n]
            => s_{n+1} = s_n + x_n
        f_n(s_n, x_n) = f_{n+1}(s_{n+1})
        f*n(s_n, x_n) = sum_{x_n} f_n(s_n,x_n)
        '''

        N = len(nums)
        if N==1:
            if nums[0]:
                return int(abs(target) == abs(nums[0]))
            else:
                return 2
        
        S=sum(nums)
        if abs(target) > S: return 0

        dp = [[], [0 for _ in range(-S, S+1)]]
        dp[-1][0]=1
        
        for n in range(N-1, -1,-1):
            stage_n=[0 for _ in range(-S, S+1)]
            stage_np1=dp[1]

            num_n = nums[n]

            for s_n in range(-S, S+1):
                F=[0,0]
                x_n=-num_n
                s_np1=s_n+x_n
                f=stage_np1[s_np1]
                F[0]=f
                x_n=num_n
                s_np1=s_n+x_n
                f=stage_np1[s_np1]
                F[1]=f
                f_sum=sum(F)
                stage_n[s_n]=f_sum
                
            dp[1]=stage_n
        return dp[1][target]
