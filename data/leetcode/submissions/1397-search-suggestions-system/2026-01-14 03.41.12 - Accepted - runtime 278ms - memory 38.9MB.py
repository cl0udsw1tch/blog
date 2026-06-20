class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        M,N=len(products),len(searchWord)
        
        nodes=[{}]
        isWord=[False]

        
        for product in products:
            node=0
            for c in product:
                if c not in nodes[node]:
                    count=len(nodes)
                    nodes[node][c]=count
                    nodes.append({})
                    isWord.append(False)
                    node=count
                else:
                    node=nodes[node][c]
            isWord[node]=product

        def dfs(node,heap):

            if len(nodes[node])==0:
                heapq.heappush(heap,isWord[node])
                return

            if isWord[node]: heapq.heappush(heap,isWord[node])
            for nbr in nodes[node]:
                dfs(nodes[node][nbr], heap)
            return

        r=[]
        node=0
        for i,c in enumerate(searchWord):
            if c not in nodes[node]:
                r.extend([[] for _ in range(i,N)])
                return r
            heap,res=[],[]
            node=nodes[node][c]
            dfs(node,heap)
            for _ in range(3):
                if not heap: break    
                res.append(heapq.heappop(heap))
            r.append(res)
                
        return r
            
        
