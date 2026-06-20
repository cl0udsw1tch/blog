class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        M=len(nums)
        if M==1: return 1
        if M==2: return 2 if nums[0]!=nums[1] else 1

        dp=[[0,0] for _ in range(M)]

        dp[-1]=[1,1]
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            F1=[1] #rise
            F2=[1] #fall
            for x_m in range(m+1, M):
                if nums[x_m]-nums[m]==0: continue
                elif nums[x_m]-nums[m]>0:
                    s_mp1=1
                    F1.append(dp[x_m][s_mp1]+1)
                else:
                    s_mp1=0
                    F2.append(dp[x_m][s_mp1]+1)
            stage_m[0]=max(F1)
            stage_m[1]=max(F2)
        return max([max(stage) for stage in dp])