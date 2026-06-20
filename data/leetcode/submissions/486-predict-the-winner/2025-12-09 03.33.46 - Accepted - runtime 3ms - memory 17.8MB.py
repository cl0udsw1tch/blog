class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) considers the array of length M-m starting at s_m and
            gives the highest score difference playerA-playerB at and after 
            the current move on nums[s_m ... s_m+(M-m)], and where the current player is playerA
        s_m: current array's start index (end index = s_m + (M-m))
        x_m: which terminal chosen (s_m or s_m + (M-m))
            (x_m=s_m) s_{m+1}=s_m+1
            (x_m=s_m+(M-m)) s_{m+1}=s_m
        f_m(s_m, x_m) = nums[x_m] - f*_{m+1}(s_{m+1}))
        f*_m(s_m) = max(f_m(s_m, x_m))
        '''

        M=len(nums)
        if M==1: return True
        if M==2: return True
        if M==3: return nums[0]+nums[2] >= nums[1]

        dp=[[0 for _ in range(M)] for _ in range(M)]

        m=M-1
        stage_m=dp[m]
        for s_m in range(M):
            x_m=s_m
            stage_m[s_m]=nums[x_m]

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            for s_m in range(M):
                sz=M-m
                terminal=s_m + sz - 1
                if terminal > M-1: break
                F=[]
                for x_m in [s_m, terminal]:
                    s_mp1=s_m if x_m==terminal else s_m+1
                    f=nums[x_m] - stage_mp1[s_mp1]
                    F.append(f)
                f_max=max(F)
                stage_m[s_m]=f_max
        return dp[0][0] >= 0