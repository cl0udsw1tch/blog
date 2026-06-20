class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        M=len(points)
        if M==1:
            return 1
        points.sort(key=lambda x: x[0])
        total=0
        prev_l,prev_r=points[0][0],points[0][1]
        for m in range(M):
            curr_l,curr_r=points[m][0],points[m][1]
            if curr_l>prev_r:
                total+=1
                prev_l,prev_r=curr_l,curr_r
            else:
                prev_l,prev_r=max(prev_l,curr_l),min(prev_r,curr_r)
        total+=1
        return total

        