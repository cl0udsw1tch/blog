# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root.left and not root.right: return root

        self.LCA=None
        def dfs(node):
            if not node: return False
            if not node.left and not node.right: return node==p or node==q

            if self.LCA: return False

            if node==p or node==q:
                l,r = dfs(node.left), dfs(node.right)
                if l or r: self.LCA=node
                return True
            else:
                l,r = dfs(node.left), dfs(node.right)    
                if l and r: self.LCA=node
                return l or r
        dfs(root)
        return self.LCA