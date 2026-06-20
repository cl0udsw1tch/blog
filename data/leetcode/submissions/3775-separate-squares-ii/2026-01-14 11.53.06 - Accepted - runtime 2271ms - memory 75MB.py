class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        M=len(squares)

        events=[]
        for square in squares:
            x,y,l=square[0],square[1],square[2]
            x1,x2,y1,y2=x,x+l,y,y+l
            e1=(y1, 1, x1, x2)
            e2=(y2,-1, x1, x2)
            events.append(e1)
            events.append(e2)
        events.sort(key=lambda e: (e[0], -e[1]))

        # print(events)
        
        X=set([square[0] for square in squares] +  [square[0]+square[2] for square in squares])
        X=sorted(list(X))
        x_to_idx={v:i for i,v in enumerate(X)}

        n_leaves=len(X)-1
        N = 4 * n_leaves
        count = [0] * N
        covered_len = [0] * N

        def update(v,L,R,ul,ur,val):
            if ul>R or ur<L: # neither this interval or its children need updating
                return

            if ul<=L and R<=ur: # this interval needs updating (lazy, ignore children)
                count[v]+=val
            else:
                MID=(L+R)//2
                update(v*2,     L, MID,   ul,ur,val)
                update(v*2+1,   MID+1, R, ul,ur,val)
            
            if count[v]>0:
                covered_len[v]=X[R+1]-X[L]
            else:
                covered_len[v]=(covered_len[v*2]+covered_len[v*2+1]) if R>L else 0

        pref_sum=[]
        prev_y=events[0][0]
        for e in events:
            y,s,x1,x2=e
            dy=y-prev_y
            area=dy*(covered_len[1])
            pref_sum.append((pref_sum[-1] if pref_sum else 0) +area)
            update(1, 0,n_leaves-1, x_to_idx[x1], x_to_idx[x2]-1, s)
            prev_y=y

        # print(pref_sum)

        l,r=-1,2*M
        target=pref_sum[-1]/2
        while l+1<r:
            MID=(l+r)//2
            # print(l,r,MID)
            if pref_sum[MID]<target:
                l=MID
            else:
                r=MID
        # print(l,r)
        # print(events[r][0],events[l][0])
        return events[l][0]+((target-pref_sum[l])/(pref_sum[r]-pref_sum[l]))*(events[r][0]-events[l][0])
