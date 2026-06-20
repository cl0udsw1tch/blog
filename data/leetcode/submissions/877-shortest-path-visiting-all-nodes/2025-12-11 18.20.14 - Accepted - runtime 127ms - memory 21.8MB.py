

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        '''
        f*(mask, node) gives the shortest path to node that sets the bits in mask
        s: (mask, node)
        x: neighbor => x'(s')=s (forward induction)
        f(s, x') = f*(s')+1
        f*(s) = \min_{x': x'(s')=s} (f(s, x')) = f(s, x'*) = f*(s'*)+1 (x'*=s'* given automatically by BFS iteration)
        '''
        N=len(graph)
        if N<=2: return N-1

        memo={}
        for node in range(N):
            memo[(node, 1<<node)]=0

        q=deque(list(zip(range(N), [1<<n for n in range(N)])))
        
        while q:
            s_p_star=q.popleft()
            node_p_star, mask_p_star = s_p_star
            if mask_p_star==2**N-1: return memo[s_p_star]

            for x_p_star in graph[node_p_star]:
                node=x_p_star
                mask=mask_p_star | (1<<node)
                s=(node, mask)
                if s in memo: continue
                f_star=memo[s_p_star]+1
                memo[s]=f_star
                q.append(s)



            