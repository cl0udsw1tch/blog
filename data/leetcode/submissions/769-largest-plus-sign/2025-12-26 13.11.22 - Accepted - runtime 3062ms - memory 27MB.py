class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        if n==1:
            return int(len(mines)==0)
        if n==2:
            return int(len(mines)<4)
        if len(mines)==0:
            return math.ceil(n/2)
        
        memo1=[[0 for _ in range(n)] for _ in range(n)]
        memo2=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                memo1[i][j]=min(abs(i+1), abs(n-i), abs(j+1), abs(n-j))
                memo2[i][j]=memo1[i][j]
        for mine in mines: 
            memo1[mine[0]][mine[1]]=0
            memo2[mine[0]][mine[1]]=0

        q=deque(mines)
        visited=[[False for _ in range(n)] for _ in range(n)]
        for mine in mines: visited[mine[0]][mine[1]]=True
        while q:
            curr=q.popleft()
            i,j=curr[0],curr[1]
            for x,y in [(0,-1), (0,1)]:
                i_p,j_p=i+x,j+y
                if j_p<0 or j_p>n-1: continue
                if visited[i_p][j_p]: continue
                memo1[i_p][j_p]=min(memo1[i_p][j_p],memo1[i][j]+1)
                visited[i_p][j_p]=True
                q.append([i_p, j_p])

        q=deque(mines)
        visited=[[False for _ in range(n)] for _ in range(n)]
        for mine in mines: visited[mine[0]][mine[1]]=True
        while q:
            curr=q.popleft()
            i,j=curr[0],curr[1]
            for x,y in [(1,0), (-1,0)]:
                i_p,j_p=i+x,j+y
                if i_p>n-1 or i_p<0: continue
                if visited[i_p][j_p]: continue
                memo2[i_p][j_p]=min(memo2[i_p][j_p], memo2[i][j]+1)
                visited[i_p][j_p]=True
                q.append([i_p, j_p])

        return max([max([min(memo1[i][j], memo2[i][j]) for j in range(n)]) for i in range(n)])
 
