class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        M=len(arr)

        dp=[[(0,0,0)] for _ in range(M)]

        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]

            if arr[m+1]>arr[m]:
                f=(1+stage_mp1[0][0], 0)
                pivot=m+f[0]
                if dp[pivot][0][1]>0:
                    f=f+(f[0]+dp[pivot][0][1]+1,)
                else:
                    f=f+(0,)
                stage_m[0]=f
            elif arr[m+1]<arr[m]:
                f=(0, stage_mp1[0][1]+1,0)
                stage_m[0]=f
            else:
                stage_m[0]=(0,0,0)
        
        return max([stage[0][2] for stage in dp])
        


