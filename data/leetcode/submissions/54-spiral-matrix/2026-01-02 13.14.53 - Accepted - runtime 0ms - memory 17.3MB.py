class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        M,N=len(matrix),len(matrix[0])
        r=[0]*(M*N)

        memo={}
        X=[(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(s):
            m,n,i,dir,arr=s
            arr[i]=matrix[m][n]
            memo[(m,n)]=True
            for x in [dir, (dir+1) % 4]:
                m_p,n_p=m+X[x][0],n+X[x][1]
                if not (0<=m_p<M) or not (0<=n_p<N):
                    continue
                if (m_p,n_p) in memo: continue
                s_p=m_p,n_p,i+1,x,arr
                dfs(s_p)
                break
        dfs((0,0,0,0,r))
        return r
                