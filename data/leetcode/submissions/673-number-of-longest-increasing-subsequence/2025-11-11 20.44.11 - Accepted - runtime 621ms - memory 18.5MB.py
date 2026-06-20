class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        stage_n: n=0...N-1 subproblem solves problem for nums[n...N-1]
        s_n: current index
        x_n: index of nearest next element in increasing subsequence starting from s_n
            => s_n'=x_n
        f_n(s_n, x_n) = (1+ {f*_n'(s_n')[0] if exists else 0}, f*_n'(s_n')[1])
        f*_n(s_n) = max_{x_n, first element} f_n(s_n, x_n)

        '''

        N=len(nums)
        if N==1:
            return 1
        
        dp=[[(1,1)] for _ in range(N)]
        dp[-1][0]=(1,1)

        for n in range(N-2,-1,-1):
            stage_n=dp[n]
            s_n=n
            f_max=1
            f_max_count=1
            for x_n in range(n+1, N):
                s_np1=x_n
                stage_np1=dp[s_np1]
                if not nums[s_np1] > nums[s_n]:
                    continue
                f=1+stage_np1[0][0]
                f_count=stage_np1[0][1]
                if f > f_max:
                    f_max=f
                    f_max_count=f_count
                elif f==f_max:
                    f_max_count+=f_count
            stage_n[0]=(f_max, f_max_count)
        
        max_len = max(dp, key = lambda stage : stage[0][0])[0][0]
        max_len_count = sum([stage[0][1] if stage[0][0] == max_len else 0 for stage in dp])
        return max_len_count
        