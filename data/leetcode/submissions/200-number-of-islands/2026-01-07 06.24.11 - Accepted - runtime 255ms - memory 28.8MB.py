class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N=len(grid),len(grid[0])
        if M==1 and N==1: return int(grid[0][0]=="1")

        count=0
        seen={}
        for m in range(M):
            for n in range(N):

                if grid[m][n]=="0": continue
                if (m,n) in seen: continue

                q=deque([(m,n)])
                seen[(m,n)]=True
                while q:
                    i,j=q.popleft()
                    for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                        i_p,j_p=i+x,j+y
                        if not (0<=i_p<M) or not (0<=j_p<N): continue
                        if grid[i_p][j_p]=="0": continue
                        if (i_p,j_p) in seen: continue
                    
                        q.append((i_p,j_p))
                        seen[(i_p,j_p)]=True
                count+=1

        return count
        