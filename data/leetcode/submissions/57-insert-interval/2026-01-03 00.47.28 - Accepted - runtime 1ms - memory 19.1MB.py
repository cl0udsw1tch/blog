class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        M=len(intervals)
        if M==0:
            return [newInterval]
 
        
        r=[]
        m=0
        new_l,new_r=newInterval[0],newInterval[1]
        while m<M and intervals[m][1]<new_l:
            r.append(intervals[m])
            m+=1
        if m==M:
            r.append(newInterval)
            return r

        prev_l,prev_r=new_l,new_r
        while m<M and intervals[m][0]<=prev_r:
            prev_l,prev_r=min(prev_l,intervals[m][0]),max(prev_r,intervals[m][1])
            m+=1
        r.append([prev_l,prev_r])
        if m<M:
            r.extend(intervals[m:])
        return r

