# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if not root.left and not root.right: return root.val

        self.r=float('inf')

        def dfs(node):
            if not node: return (0,0)
            if not node.left and not node.right: return (node.val, node.val)

            n_min,n_max=node.val,node.val
            if node.left:
                c_min,c_max=dfs(node.left)
                n_min=c_min
                self.r=min(self.r, abs(node.val-c_max))
            if node.right:
                c_min,c_max=dfs(node.right)
                n_max=c_max
                self.r=min(self.r, abs(node.val-c_min))
            return n_min,n_max



        dfs(root)
        return self.r
                