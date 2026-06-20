# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if not root.left and not root.right: return 1
        def dfs(node):
            if not node: return 0
            if not node.left and not node.right: return 1

            return 1 + dfs(node.left) + dfs(node.right)
            
        return dfs(root)