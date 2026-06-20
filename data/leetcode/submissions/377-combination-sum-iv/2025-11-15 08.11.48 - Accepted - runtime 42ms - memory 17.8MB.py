class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        stage_n: n = 0...target subproblem f*_n(s_n) solves problem for target n and last coin s_n
        s_n: last coin
        x_n: 2nd last coin
        => s_{n+1} =  x_n 
        f_n(s_n, x_n) = f*_{n+1}(s_{n+1})
        f*_n(s_n, x_n) = sum(f_n(s_n, x_n))

        '''

        N=len(nums)
        if N==1:
            return int(target % nums[0] == 0)

        dp=[[0] for _ in range(target + 1)]
        dp[0][0]=1

        for n in range(1,target+1):
            stage_n=dp[n]
            stage_np1=dp[n-1]
            for s_n in range(0,N):
                # F=[0 for _ in range(N)]
                # for x_n in range(0,N):
                #     F[x_n] = dp[n-nums[s_n]][x_n] if n>=nums[s_n] else 0
                # stage_n[s_n]=sum(F)
                stage_n[0] += (dp[n-nums[s_n]][0] if n>=nums[s_n] else 0)

        return sum(dp[target])