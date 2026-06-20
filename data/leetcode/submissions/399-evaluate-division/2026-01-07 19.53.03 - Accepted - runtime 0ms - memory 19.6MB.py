class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        M,N=len(equations),len(queries)

        nodes=defaultdict(list)
        for i,edge in enumerate(equations):
            a,b=edge[0],edge[1]
            nodes[a].append((b, values[i]))
            nodes[b].append((a, 1/values[i]))
        
        r=[-1]*N
        for i,query in enumerate(queries):
            c,d=query[0],query[1]
            if c not in nodes or d not in nodes:
                continue
            if c==d:
                r[i]=1
                continue
            q=deque([c])
            seen={c: 1}
            while q:
                curr=q.popleft()
                for neighbor,val in nodes[curr]:
                    if neighbor in seen: continue
                    seen[neighbor]=seen[curr]*val
                    if neighbor==d:
                        r[i]=seen[neighbor]
                        break
                    q.append(neighbor)
        return r
                
                    
            