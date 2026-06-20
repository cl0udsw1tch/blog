class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        stage_n: n=0...N-1, subproblem solves for nums[n...N] all capacities w=0...W=sum(nums)/2 that can be 
                made from these elements. That is, stage_n[w]=True if capacity can be made, false otherwise
        s_n: the current sum w = 0...W
        x_n: choosing nums[n], and using nums[n...N] to make w, or ignoring nums[n] and using nums[n+1..N] to    
                make s_n
            => s_{n+1} = s_n+x_n
            => choosing nums[n]: x_n= -nums[n] => s_{n+1}=s_n-nums[n]       (if feasible i.e >= 0)
            => skipping nums[n]: x_n= 0        => s_{n+1}=s_n
        f_n(s_n, x_n) = f_{n+1}(s_{n+1})
        f*_n(s_n) = ANY_{x_n}{f_n(s_n, x_n)} for feasible x_n


        '''

        N=len(nums)
        if N==1: return False
        if N==2: return nums[0]==nums[1]
        S=sum(nums)
        if S % 2: return False
        W=S//2

        dp=[[False for _ in range(W+1)],[False for _ in range(W+1)]]
        dp[-1][0]=True
      

        for n in range(N-1,-1,-1):
            stage_n=dp[0]
            stage_np1=dp[1]
            num_n=nums[n]
            for s_n in range(W+1):
                F=[False,False]
                x_n = 0
                s_np1=s_n+x_n
                f = stage_np1[s_np1]
                F[0]=f
                
                if s_n>=num_n:
                    x_n = -num_n
                    s_np1 = s_n+x_n
                    f = stage_np1[s_np1]
                    F[1]=f

                f_any=any(F)
                stage_n[s_n]=f_any
            dp[1]=stage_n
            dp[0]=[False for _ in range(W+1)]

        return dp[1][W]
