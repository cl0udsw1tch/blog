# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        stage_m: subproblem f*_m() solves the problem of a max *directed* path (parent->child edges only) for root=node_m
        s_m: single state
        x_m: going down left or right child, or neither
        f*_m() = max(f*_{ml}()+1,f*_{mr}()+1,0)

        => longest path will contain two directed paths starting at the same parent, or one directed path
         '''

        if not root.left and not root.right:
            return 0

        self.longestPathNodes=1
        memo={}
        def dfs(node):
            if node in memo: return
            if not node:
                memo[node]=0
                return 
            if not node.left and not node.right:
                memo[node]=1
                return
            

            dfs(node.left)
            dfs(node.right)
            F_left,F_right=memo[node.left],memo[node.right]
            F=[F_left+1,F_right+1,1]

            f_max=max(F)
            memo[node]=f_max

            self.longestPathNodes=max(self.longestPathNodes, F_left+F_right+1, f_max)

        dfs(root)

        return self.longestPathNodes-1
