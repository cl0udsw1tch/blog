class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        stage_n subproblem: n=1...d finding the optimal schedule for the last n days
        s_n: the index of first job scheduled for day d-n+1
        x_n: the number of jobs scheduled for the current day
            => s_{n+1} = s_n + x_n
        f_n(s_n, x_n) = max{s_n...s_n+x} + f*_{n+1}(s_{n+1})
        f*_n(s_n) = max_{x_n} ( f_n(s_n, x_n))

        '''

        if d > len(jobDifficulty):
            return -1
        if d == len(jobDifficulty):
            return sum(jobDifficulty)
        if d==1:
            return max(jobDifficulty)

        
        dp = [[], []]
        N=len(jobDifficulty)

        for s_n in range(d-1, N):
            dp[1].append(max(jobDifficulty[s_n:]))

        for n in range(2,d):
            stage_n=dp[0]
            stage_np1=dp[1]
            num_prev_stages=d-n
            num_proc_stages=n-1
            for s_n in range(num_prev_stages, N-num_proc_stages):
                F=[]
                f_min=None
                for x_n in range(1, (N-num_proc_stages)-s_n+1):
                    s_np1=s_n+x_n
                    num_prev_stages_np1=num_prev_stages+1
                    f=max(jobDifficulty[s_n:s_np1]) + stage_np1[s_np1-(num_prev_stages_np1)]
                    F.append(f)
                f_min=min(F)
                stage_n.append(f_min)

            dp[1]=stage_n
            dp[0]=[]
            print(dp)
        
        s_n=0
        F=[]
        f_min=None
        numPrevStages=0
        numProcStages=d-1
        numPrevStages_np1=numPrevStages+1
        for x_n in range(1, N-numProcStages+1):
            s_np1=x_n
            f=max(jobDifficulty[:s_np1]) + dp[1][s_np1-numPrevStages_np1]
            F.append(f)
        f_min=min(F)

        print(f_min)
        return f_min

