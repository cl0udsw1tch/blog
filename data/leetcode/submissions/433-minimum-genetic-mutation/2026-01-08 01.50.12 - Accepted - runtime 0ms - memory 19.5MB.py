class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank: return -1
        adj_map=defaultdict(list)

        for a in bank:
            for b in bank:
                if a==b: continue
                if len([i for i in range(8) if a[i]!=b[i]])==1:
                    adj_map[a].append(b)
                    adj_map[b].append(a)
        if startGene not in bank:
            for b in bank:
                if len([i for i in range(8) if startGene[i]!=b[i]])==1:
                    adj_map[startGene].append(b)
                    adj_map[b].append(startGene)
        
        q=deque([startGene])
        seen={startGene:0}

        while q:
            curr=q.popleft()
            count=seen[curr]
            for neighbor in adj_map[curr]:
                if neighbor in seen: continue
                q.append(neighbor)
                seen[neighbor]=count+1
                if neighbor==endGene: return seen[neighbor]
        return -1
        
