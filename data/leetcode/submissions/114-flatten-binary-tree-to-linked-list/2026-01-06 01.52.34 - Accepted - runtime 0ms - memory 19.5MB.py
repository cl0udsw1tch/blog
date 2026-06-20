# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return None, None

            if not node.left and not node.right: return node, node
        
            left_branch,left_tail=dfs(node.left)
            right_branch,right_tail=dfs(node.right)

            if left_branch:
                node.right=left_branch
                left_tail.right=right_branch
            else:
                node.right=right_branch
            node.left=None

            tail=right_tail if right_branch else left_tail
      
            return node,tail

        return dfs(root)[0]
        