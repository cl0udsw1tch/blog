# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return

            if not node.left and not node.right:
                return

            dfs(node.left)
            dfs(node.right)
            node_left=node.left
            node.left=node.right
            node.right=node_left
            return

        dfs(root)
        return root