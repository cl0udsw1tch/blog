class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        min_x = min(x1 for x1,_,_,_ in rectangles)
        min_y = min(y1 for _,y1,_,_ in rectangles)
        max_x = max(x2 for _,_,x2,_ in rectangles)
        max_y = max(y2 for _,_,_,y2 in rectangles)

        area_sum = sum((x2-x1)*(y2-y1) for x1,y1,x2,y2 in rectangles)
        if area_sum != (max_x - min_x) * (max_y - min_y):
            return False

        events=[]
        for rectangle in rectangles:
            x1,y1,x2,y2=tuple(rectangle)
            e1=x1,1,y1,y2
            e2=x2,-1,y1,y2
            events.append(e1)
            events.append(e2)
        events.sort(key=lambda e: (e[0], e[1]))
        Y=sorted(list(set([e[2] for e in events]+[e[3] for e in events])))
        y_to_idx={v:i for i,v in enumerate(Y)}
        # n_leaves=len(Y)-1
        # N=4*n_leaves
        # count=[0]*N
        # covered=[False] * N
        # has_overlap=[False] * N

        # def update(v,L,R,e_y1,e_y2,e_s):
        #     #print(v,L,R,e_y1,e_y2)
        #     if R<e_y1 or L>e_y2:
        #             return
        #     if L==R:
        #         count[v]+=s
        #     else:
                
        #         MID=(L+R)//2
        #         update(v*2,L,MID,e_y1,e_y2,e_s)
        #         update(v*2+1,MID+1,R,e_y1,e_y2,e_s)
            
        #     if L==R: #LEAF
        #         #print(v,L,R,count[v])
        #         covered[v]=True if count[v]>0 else False
        #         has_overlap[v]=True if count[v]>1 else False
        #     else:
        #         covered[v]=(covered[v*2] and covered[v*2+1]) if L<R else False
        #         has_overlap[v]=(has_overlap[v*2] or has_overlap[v*2+1]) if L<R else False
        
        
        y_int_map=defaultdict(int)

        for e in events:
            x,s,y1,y2=e
            for i in range(y_to_idx[y1], y_to_idx[y2]):
                y_int_map[i]+=s
                if y_int_map[i]>1: return False
                i+=1
        events=[]
        for rectangle in rectangles:
            x1,y1,x2,y2=tuple(rectangle)
            e1=y1,1,x1,x2
            e2=y2,-1,x1,x2
            events.append(e1)
            events.append(e2)
        events.sort(key=lambda e: (e[0], e[1]))
        X=sorted(list(set([e[2] for e in events]+[e[3] for e in events])))
        x_to_idx={v:i for i,v in enumerate(X)}
        prev_y=events[0][0]
        x_int_map=defaultdict(int)

        for e in events:
            y,s,x1,x2=e
            for i in range(x_to_idx[x1], x_to_idx[x2]):
                x_int_map[i]+=s
                if x_int_map[i]>1: return False
                i+=1

        
        return True