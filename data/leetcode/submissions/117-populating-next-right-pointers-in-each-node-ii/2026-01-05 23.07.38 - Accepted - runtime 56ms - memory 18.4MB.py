"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return root
        if not root.left and not root.right: return root

        q=deque([root])
        seen={root: 0} #depth
        while q:
            node=q.popleft()

            for child in [node.left,node.right]:
                if not child: continue
                if q and seen[q[-1]]==seen[node]+1: q[-1].next=child
                q.append(child)
                seen[child]=seen[node]+1
            
        return root

                
            