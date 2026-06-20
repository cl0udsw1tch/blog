# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        if not root.left and not root.right: return [[root.val]]

        q=deque([root])
        r=[]
        forward=True
        while q:
            n_row=len(q)
            level=[0]*n_row
            for n in (range(n_row) if forward else range(n_row-1,-1,-1)):
                node=q.popleft()

                level[n]=node.val
                for child in [node.left, node.right]:
                    if not child: continue
                    q.append(child)
            r.append(level)
            forward=not forward
        return r