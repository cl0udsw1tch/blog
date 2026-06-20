class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            intervals.sort(key=lambda interval: interval[0])

            M=len(intervals)
            if M==1: return 0

            dp=[[(0,float('inf'))] for _ in range(M)]
            dp[-1][0]=(0,M-1)

            for m in range(M-2,-1,-1):
                stage_m=dp[m]
                stage_mp1=dp[m+1]
                s_m=0
                s_mp1=0
                nextInterval=intervals[stage_mp1[s_mp1][1]]
                f1 = int(not (intervals[m][1] <= nextInterval[0])) + stage_mp1[s_mp1][0]
                f2 = stage_mp1[s_mp1][1] if not (intervals[m][1] <= nextInterval[0]) else m
                stage_m[s_m]=f1,f2

            return dp[0][0][0]

