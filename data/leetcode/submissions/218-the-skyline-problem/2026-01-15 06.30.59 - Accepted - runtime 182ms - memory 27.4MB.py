class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events=[]
        for building in buildings:
            x1,x2,h=building[0],building[1],building[2]
            e1=x1,1,h
            e2=x2,-1,h
            events.append(e1)
            events.append(e2)
        events.sort(key=lambda e: (e[0], -e[1]))
        Y=sorted(list(set([building[2] for building in buildings])))
        y_to_idx={v:i for i,v in enumerate(Y)}

        n_leaves=len(Y)
        N=4*n_leaves
        count = [0] * N
        height = [0] * N

        def update(v,L,R, e_h,e_s):


            if R<=e_h:
                count[v]+=e_s
            elif L>e_h:
                return 
            else:
                MID=(L+R)//2
                update(2*v, L, MID, e_h,e_s)
                update(2*v+1, MID+1, R, e_h,e_s)
            
            if count[v]>0:
                height[v]=Y[R] if L<=R else 0
            else:
                height[v]=max(height[v*2], height[v*2+1]) if L<R else 0
        
        q=deque([])
        prev_x=events[0][0]
        for e in events:
            top=height[1]
            x,s,h=e
            if x-prev_x>0: 
                q.append([prev_x,top])

            update(1, 0, n_leaves-1, y_to_idx[h], s)
            prev_x=x
        q.append([x,0])
        key_points=[q.popleft()]
        prev_h=key_points[0][1]
        while q:
            curr=q.popleft()
            curr_x,curr_h=curr[0],curr[1]
            if curr_h==prev_h: continue
            prev_h=curr_h
            key_points.append([curr_x, curr_h])

        return key_points



