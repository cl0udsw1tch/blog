class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        events=[]
        for interval in firstList+secondList:
            l,r=tuple(interval)
            e1=l,1
            e2=r,-1
            events.append(e1)
            events.append(e2)
        
        events.sort(key=lambda e: (e[0], -e[1]))
        intersections=[]
        n_active=0
        current=[]
        for e in events:
            x,s=e
            if s==1:
                n_active+=1
                if n_active==2:
                    current.append(x)
            else:
                n_active-=1
                if n_active==1:
                    current.append(x)
            if len(current)==2:
                intersections.append(current)
                current=[]
        
        return intersections
        
