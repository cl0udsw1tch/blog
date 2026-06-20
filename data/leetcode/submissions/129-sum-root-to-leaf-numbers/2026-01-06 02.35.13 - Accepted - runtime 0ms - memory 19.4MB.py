# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if not root.left and not root.right: return root.val

        def dfs(node, curr):
            if not node:
                return curr
            if not node.left and not node.right: return curr*10 + node.val

            F=0
            for child in [node.left,node.right]:
                if not child: continue
                F+=dfs(child, curr*10 + node.val)
            return F

        return dfs(root,0)