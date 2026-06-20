class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        DIES_LIVES=-1
        DIES_DIES=-2
        LIVES_DIES=-3
        LIVES_LIVES=-4

        M,N=len(board),len(board[0])
        if M==1 and N==1:
            board[0][0]=0
            return 
            
        for m in range(M):
            for n in range(N):
                curr=board[m][n]
                n_neighbors=0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if not (0<=m+x<M) or not (0<=n+y<N):continue
                        if x==0 and y==0: continue
                        neighbor=board[m+x][n+y]
                        n_neighbors+=(1 if neighbor in [LIVES_DIES, LIVES_LIVES, 1] else 0)
                if n_neighbors<2:
                    board[m][n]=DIES_DIES if curr==0 else LIVES_DIES
                elif n_neighbors==2:
                    board[m][n]=LIVES_LIVES if curr==1 else DIES_DIES
                elif n_neighbors==3:
                    board[m][n]=LIVES_LIVES if curr==1 else DIES_LIVES
                elif n_neighbors>3:
                    board[m][n]=DIES_DIES if curr==0 else LIVES_DIES
        for m in range(M):
            for n in range(N):
                curr=board[m][n]
                board[m][n]=0 if curr in [LIVES_DIES, DIES_DIES] else 1
        



