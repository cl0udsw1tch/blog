# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root: return 0
        if not root.left and not root.right: return root.val

        node=root
        count=0
        while node:
            if not node.left:
                count+=1
                if count==k:return node.val
                node=node.right
            else:
                prev=node.left
                while prev.right and prev.right!=node:
                    prev=prev.right

                if not prev.right:
                    prev.right=node
                    node=node.left
                else:
                    prev.right=None
                    count+=1
                    if count==k: return node.val
                    node=node.right
           
