# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        if not root.left and not root.right: return [root.val]

        r=[root.val]
        parent=root
        parent.next=None
        
        while parent:
            first_child=None

            while parent and not parent.left and not parent.right:
                parent=parent.next
            if not parent:
                return r
            else:
                first_child=parent.left if parent.left else parent.right

            l_child=first_child
            while l_child:
                r_child=parent.right if l_child==parent.left else None
                
                if not r_child:
                    parent=parent.next
                    while not r_child and parent and not parent.left and not parent.right:
                        parent=parent.next

                    if not parent:
                        r.append(l_child.val)
                    else:
                        r_child=parent.left if parent.left else parent.right

                l_child.next=r_child
                l_child=r_child

            parent=first_child

        return r
                

