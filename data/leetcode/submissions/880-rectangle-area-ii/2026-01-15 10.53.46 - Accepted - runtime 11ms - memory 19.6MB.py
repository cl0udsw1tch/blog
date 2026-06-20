class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD=10**9+7
        events=[]
        for rect in rectangles:
            x1,y1,x2,y2=tuple(rect)
            e1=x1,1,y1,y2
            e2=x2,-1,y1,y2
            events.append(e1)
            events.append(e2)
        events.sort(key=lambda e: (e[0],e[1]))
        Y=sorted(list(set([e[2] for e in events]+[e[3] for e in events])))
        y_to_idx={v:i for i,v in enumerate(Y)}
        n_leaves=len(Y)-1
        N=n_leaves*4
        count=[0]*N
        covered_len=[0]*N

        def update(v,L,R,el,er,es):
            if el<=L and R<=er:
                count[v]+=es
            elif R<el or er<L:
                return
            else:
                MID=(L+R)//2
                update(v*2, L, MID, el,er,es)
                update(v*2+1, MID+1, R, el,er,es)
            
            if count[v]>0:
                covered_len[v]=Y[R+1]-Y[L] if L<=R else 0
            else:
                covered_len[v]=(covered_len[v*2]+covered_len[v*2+1]) if L<R else 0
        
        prev_x=events[0][0]
        total_area=0
        for e in events:
            x,s,y1,y2=e
            dx=x-prev_x
            if dx:
                total_area+=dx*covered_len[1]
            update(1, 0, n_leaves-1, y_to_idx[y1], y_to_idx[y2]-1, s)
            prev_x=x
        return total_area % MOD
            