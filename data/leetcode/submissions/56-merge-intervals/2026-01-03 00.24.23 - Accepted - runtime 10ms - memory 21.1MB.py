class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        M=len(intervals)
        if M==1: return intervals

        intervals.sort(key=lambda interval: interval[0])
        r=[]
        prev_l,prev_r=intervals[0][0], intervals[0][1]
        for m in range(1,M):
            curr_l,curr_r=intervals[m][0], intervals[m][1]
            if curr_l<=prev_r:
                prev_r=max(prev_r,curr_r)
            else:
                r.append([prev_l,prev_r])
                prev_l,prev_r=curr_l,curr_r
        r.append([prev_l, prev_r])
        return r
        