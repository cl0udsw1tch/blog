class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M=len(mat)
        N=len(mat[0])

        if M==1 and N==1: return [[0]]

        '''

        q=deque([])
        r=[[float('inf') for _ in range(N)] for _ in range(M)]
        visited=[[False for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for n in range(N):
                if mat[m][n]==0:
                    q.append((m,n))
                    r[m][n]=0
                    visited[m][n]=True

        while q:
            m,n=q.popleft()
            
            for x,y in [(1,0),(-1,0),(0,1), (0,-1)]:
                m_p,n_p=m+y,n+x
                if m_p < 0 or m_p > M-1 or n_p < 0 or n_p > N-1: continue
                if visited[m_p][n_p]: continue

                if mat[m_p][n_p]==0:
                    r[m_p][n_p]=0
                else:
                    r[m_p][n_p]=r[m][n]+1

                
                q.append((m_p,n_p))
                visited[m_p][n_p]=True
        return r
        '''
        INF = M + N  

        memo1 = {}
        memo2 = {}

        def dp1(s):
            i,j=s
            if s in memo1: return
            if mat[i][j] == 0:
                memo1[s]=0
                return

            F=[float('inf')]
            for x,y in [(-1,0), (0,-1)]:
                i_p,j_p=i+x,j+y
                if i_p<0 or j_p<0: continue
                s_p=i_p,j_p
                dp1(s_p)
                F.append(memo1[s_p]+1)
            memo1[s] = min(F)

        def dp2(s):
            i,j=s
            if s in memo2: return
            if mat[i][j] == 0:
                memo2[s]=0
                return

            F=[memo1[s]]
            for x,y in [(1,0), (0,1)]:
                i_p,j_p=i+x,j+y
                if i_p>M-1 or j_p>N-1: continue
                s_p=i_p,j_p
                dp2(s_p)
                F.append(memo2[s_p]+1)

            memo2[s] = min(F)

        for i in range(M):
            for j in range(N):
                dp1((i, j))

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp2((i, j))

        ans = [[memo2[(i,j)] for j in range(N)] for i in range(M)]
        
        return ans
        