class Solution:
    def candy(self, ratings: List[int]) -> int:
        M=len(ratings)
        if M==1: return 1        
    
        p=[]
        if ratings[0]<=ratings[1]:
            p.append((0,0))
        else:
            p.append((0,1))

        for m in range(1,M-1):
            if ratings[m-1]>=ratings[m]<=ratings[m+1]:
                p.append((m,0))
            elif ratings[m-1]<=ratings[m]>ratings[m+1] or ratings[m-1]<ratings[m]>=ratings[m+1]:
                p.append((m,1))
        
        if ratings[-1]<=ratings[-2]:
            p.append((M-1,0))
        else:
            p.append((M-1,1))

        Q=len(p)
        r=[0]*M
        for q in range(Q-1):
            curr,next=p[q],p[q+1]
            if curr[1]==0 and next[1]==0: # trough, trough
                for m in range(curr[0], next[0]+1):
                    r[m]=1
            elif curr[1]==0 and next[1]==1: # trough, peak
                for m in range(curr[0], next[0]+1):
                    r[m]=max(r[m], m-curr[0]+1)
            elif curr[1]==1 and next[1]==0: # peak, trough
                for m in range(next[0], curr[0]-1, -1):
                    r[m]=max(r[m], next[0]-m+1)
            elif curr[1]==1 and next[1]==1: # peak, peak
                pass

        return sum(r)

