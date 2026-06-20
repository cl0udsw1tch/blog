class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M,N=len(board),len(board[0])
        if M==1 and N==1: return

        seen={}
        for m in range(M):
            for n in range(N):

                if board[m][n]=="X": continue
                if (m,n) in seen: continue

                q=deque([(m,n)])
                _seen={}
                _seen[(m,n)]=True
                surroundable=(0<m<M-1) and (0<n<N-1)
                while q:
                    i,j=q.popleft()
                    for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                        i_p,j_p=i+x,j+y
                        if not (0<=i_p<M) or not (0<=j_p<N): continue
                        if board[i_p][j_p]=="X": continue
                        if (i_p,j_p) in _seen: continue

                        q.append((i_p,j_p))
                        _seen[(i_p,j_p)]=True
                        if surroundable and (i_p==0 or i_p==M-1 or j_p==0 or j_p==N-1):
                            surroundable=False

                for i,j in _seen:
                    if surroundable: board[i][j]="X"
                    seen[(i,j)]=True
        