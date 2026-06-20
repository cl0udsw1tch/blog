class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        stage_n: n=0...N-1 subproblem solves problem for nums[n...N]
        s_n: current index
        x_n: index of next element in longest subsequence starting from x_n, if exists
            s_n'=x_n
        f_n(s_n,x_n) = 1 + {f_n'(s_n') if x_n' else 0}
        f*_n(s_n) = max_{x_n}(f_n(s_n,x_n)) 

        '''
        N=len(nums)
        if N==1:
            return 1

        dp = [[0] for _ in range(N)]

        dp[-1][0]=1

        for n in range(N-2,-1,-1):
            stage_n=dp[n]
            s_n=n
            F=[0 for _ in range(n,N)]
            F[0]=1
            for x_n in range(n+1,N):
                s_np1=x_n
                stage_np1=dp[s_np1]
                if not nums[s_np1]>nums[s_n]: continue
                f=1+stage_np1[0]
                F[x_n-n]=f
            f_max=max(F)
            stage_n[0]=f_max
        return max(dp,key=lambda stage : stage[0])[0]

        