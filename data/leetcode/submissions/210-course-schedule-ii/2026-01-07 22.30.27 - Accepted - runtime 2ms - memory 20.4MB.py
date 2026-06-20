class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_map=defaultdict(int)
        adj_list=defaultdict(list)

        for edge in prerequisites:
            a,b=edge[0],edge[1]
            in_map[a]+=1
            adj_list[b].append(a) #a<-b

        q=deque([a for a in range(numCourses) if in_map[a]==0])
        l=[a for a in range(numCourses) if in_map[a]==0]

        while q:
            node=q.popleft()
            for neighbor in adj_list[node]:
                in_map[neighbor]-=1
                if in_map[neighbor]==0:
                    l.append(neighbor)
                    q.append(neighbor)
        return l if len(l) == numCourses else []
            