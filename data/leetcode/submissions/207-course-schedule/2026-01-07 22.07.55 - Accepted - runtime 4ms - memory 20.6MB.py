class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        out_map=defaultdict(int)
        pred_map=defaultdict(list)
        for edge in prerequisites:
            a,b=edge[0],edge[1]
            out_map[a]+=1
            pred_map[b].append(a)

        q=deque([a for a in range(numCourses) if out_map[a]==0])
        l=[a for a in range(numCourses) if out_map[a]==0]
        while q:
            node=q.popleft()
            for pred in pred_map[node]:
                out_map[pred]-=1
                if out_map[pred]==0:
                    q.append(pred)
                    l.append(pred)

        return len(l)==numCourses
