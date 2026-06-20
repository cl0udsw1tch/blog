# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        if not root.left and not root.right: return [[root.val]]

        r=[]
        q=deque([root])

        while q:
            level=[]
            n_row=len(q)

            for n in range(n_row):
                node=q.popleft()
                level.append(node.val)

                for child in [node.left, node.right]:
                    if not child: continue
                    q.append(child)
                
            r.append(level)
        return r