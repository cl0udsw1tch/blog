class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''
        stage_m: shortest path using *internmediate* (not terminal) nodes from [m...n-1] only
        s_n: iterating over ALL (i,j) and considering path connecting those nodes
        x_n: keeping the path or reducing cost by inserting node m such that the path (i,m)(m,j) exists
        f_n(s_n, x_n) ={ f*_{n+1}(s_n) \\ f*_{n+1}((i, m)) + f*_{n+1}((m, j))
        f*_n(s_n) = \min_{x_n} {f_n(s_n, x_n)}

        '''
        
        dp = [[[math.inf for _ in range(n)] for _ in range(n)],\
        [[math.inf for _ in range(n)] for _ in range(n)]]

        for edge in edges:
            if edge[2]<=distanceThreshold:
                dp[1][edge[0]][edge[1]]=edge[2]
                dp[1][edge[1]][edge[0]]=edge[2]

        stage_m=dp[0]
        stage_mp1=dp[1]
        for m in range(0, n):
            for i in range(0,n):
                if m==i: 
                    continue
                for j in range(0,n):
                    if m==j or i==j :
                        continue
                    s_m=(i,j)
                    F=[stage_mp1[s_m[0]][s_m[1]]]
                    f = stage_mp1[s_m[0]][m] + stage_mp1[m][s_m[1]]
                    F.append(f if f <= distanceThreshold else math.inf)
                    f_star=min(F)
                    stage_m[s_m[0]][s_m[1]]=f_star
            for i in range(0,n):
                if m==i: 
                    continue
                for j in range(0,n):
                    if m==j or i==j :
                        continue
                    s_m=(i, j)
                    stage_mp1[s_m[0]][s_m[1]]=stage_m[s_m[0]][s_m[1]]
                    stage_mp1[j][i]=stage_mp1[i][j]
        r=[[0,0] for _ in range(n)]     
        for i in range(0, n):
            for j in range(0,n):
                v=stage_mp1[i][j]
                if v==math.inf:continue
                r[i][0]+=1
                r[i][1]+=v
        
        r_min=(-1, math.inf)
        for i,c in enumerate(r):
            if c[0]<=r_min[1]:
                r_min=(i, c[0])
  
        return r_min[0]

