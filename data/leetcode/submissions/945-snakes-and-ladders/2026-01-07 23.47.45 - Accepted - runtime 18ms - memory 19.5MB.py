class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        N=len(board)
        q=deque([1])
        seen={}
        seen[1]=0

        while q:
            curr=q.popleft()
            count=seen[curr]
            i=N-(curr-1)//N-1
            j=(curr-1)%N if not (N-i-1)%2 else N-((curr-1)%N)-1
            for neighbor in range(curr+1,min(curr+6,N**2)+1):
                i_p=N-(neighbor-1)//N-1
                j_p=(neighbor-1)%N if not (N-i_p-1)%2 else N-((neighbor-1)%N)-1

                neighbor=neighbor if board[i_p][j_p]==-1 else board[i_p][j_p]
                if neighbor in seen: continue
                q.append(neighbor)
                seen[neighbor]=(count+1)

                if neighbor==N**2: 
                    return count+1

        return -1
        
