class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        edge_map=[{}]
        is_word=defaultdict(bool)
        count=0

        for word in words:
            N=len(word)
            node=0
            for n in range(N):
                c=word[n]
                if c in edge_map[node]:
                    node=edge_map[node][c]
                else:
                    count+=1
                    edge_map[node][c]=count
                    edge_map.append({})
                    node=count
            is_word[node]=word

        M,N=len(board),len(board[0])
        r={w: False for w in words}

        def dfs_backtrack(idx,node,curr_path):
            m,n=idx
            w=is_word[node]
            if w and not r[w]:
                r[w]=True

            for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                m_p,n_p=m+x,n+y
                if not 0<=m_p<M or not 0<=n_p<N: continue
                neighbor=board[m_p][n_p]

                if (m_p,n_p) in curr_path: continue
                if neighbor not in edge_map[node]: continue
    
                curr_path.add((m_p,n_p))
                dfs_backtrack((m_p,n_p),edge_map[node][neighbor],curr_path)
                curr_path.remove((m_p,n_p))


        for m in range(M):
            for n in range(N):
                c=board[m][n]
                if c not in edge_map[0]: continue
                dfs_backtrack((m,n),edge_map[0][c],set([(m,n)]))

        return [w for w in r if r[w]]
                        

                