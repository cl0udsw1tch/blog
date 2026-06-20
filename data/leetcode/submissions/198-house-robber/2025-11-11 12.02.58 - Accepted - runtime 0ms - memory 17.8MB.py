class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        stage_n: n = 0...N-1 subproblem solves the problem for houses n...N-1
        s_n: current house
        x_n: rob or skip s_n
            => s_{n+1} = s_{n+2} (if rob) or s_{n+1} (if skip)
        f_n(s_n, x_n) = nums[s_n] + f*_{n+2}(s_{n+2}) (if rob)
                      = f*_{n+1}(s_{n+1}) (if skip)
        f*n(s_n) = max_{x_n}(f_n{s_n,x_n})


        '''
        N=len(nums)
        if N==1: return nums[0]
        if N==2: return max(nums)

        dp=[[None],[max(nums[-2], nums[-1])],[nums[-1]]]
   
        for n in range(N-3,-1,-1):
            stage_n=dp[0]
            stage_np1=dp[1]
            stage_np2=dp[2]

            s_n=nums[n]
            F=[s_n+stage_np2[0], stage_np1[0]]
            f_max=max(F)
            stage_n[0]=f_max

            dp[2]=stage_np1
            dp[1]=stage_n
            dp[0]=[None]

        return dp[1][0]