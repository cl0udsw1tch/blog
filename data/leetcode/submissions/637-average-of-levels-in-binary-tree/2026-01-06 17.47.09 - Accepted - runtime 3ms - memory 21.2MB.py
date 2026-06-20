# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root: return [0]
        if not root.left and not root.right: return [root.val]

        r=[]
        q=deque([root])

        while q:
            n_row = len(q)
            total = 0

            for n in range(n_row):
                node = q.popleft()
                total+=node.val

                for child in [node.left, node.right]:
                    if not child: continue
                    q.append(child)

            total/=n_row
            r.append(total)
            
        return r

