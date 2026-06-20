# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        stage_m: subproblem f*_m() solves the problem of a max *directed* path (parent->child edges only) for root=node_m
        s_m: single state
        x_m: going down left or right child, or neither
        f*_m() = max(f*_{ml}(),f*_{mr}(),0) + node_m.val

        => optimal path will contain two directed paths starting at the same parent, or one directed path
         '''

        if not root.left and not root.right:
            return root.val

        self.maxVal=root.val

        def dfs(node):
            if not node: return
            if not node.left and not node.right:
                self.maxVal=max(self.maxVal, node.val)
                return node.val

            F=[0]
            if node.left:
                F.append(dfs(node.left))
            if node.right:
                F.append(dfs(node.right))
            f_max=node.val+max(F)
            f_sum=node.val+sum(F)
            self.maxVal=max(self.maxVal, f_max, f_sum)
            return f_max

        dfs(root)
        return self.maxVal
            

           


