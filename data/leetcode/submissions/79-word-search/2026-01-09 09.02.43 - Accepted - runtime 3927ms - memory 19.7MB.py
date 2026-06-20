class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        M,N,W=len(board),len(board[0]),len(word)
        X=[(0,1), (0,-1), (1,0), (-1,0)]


        def backtrack(idx, i, curr):
            if i==W: return True
            m,n=idx

            for x,y in X:
                m_p,n_p=m+x,n+y
                if not (0<=m_p<M and 0<=n_p<N): continue
                if (m_p,n_p) in curr: continue
                c=board[m_p][n_p]
                if c!=word[i]: continue
                curr.add((m_p,n_p))
                r=backtrack((m_p,n_p),i+1, curr)
                curr.remove((m_p,n_p))
                if r: 
                    return True
            return False

        for m in range(M):
            for n in range(N):
                if board[m][n]!=word[0]: continue
                if backtrack((m,n),1,set([(m,n)])):
                    return True
        return False