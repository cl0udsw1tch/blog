# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        if not root.left and not root.right: return True

        node=root
        last=-float('inf')
        while node:
            if not node.left:
                if not node.val>last: return False
                last=node.val
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
                   
                    if not node.val>last: return False
                    
                    last=node.val
                    node=node.right
                    
        return True