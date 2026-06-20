class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9,3):
            for j in range(0,9,3):
                square=0
                for k in range(9):
                    curr=board[i+k//3][j+k%3]
                    if curr==".":continue
                    if (1<<int(curr))&square: return False
                    square=(1<<int(curr))|square
        for i in range(9):
            row=0
            for j in range(9):
                curr=board[i][j]
                if curr==".":continue
                if (1<<int(curr))&row: return False
                row=(1<<int(curr))|row
        for j in range(9):
            col=0
            for i in range(9):
                curr=board[i][j]
                if curr==".":continue
                if (1<<int(curr))&col: return False
                col=(1<<int(curr))|col
        return True
        