"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        if not node: return None
        if not node.neighbors: return Node(val=node.val)

        clone_node=Node(val=node.val)
        q=deque([(node,clone_node)])
        seen={node: clone_node}
        
        while q:
            curr,clone=q.popleft()
            clone.neighbors=[None]*len(curr.neighbors)
            for i,neighbor in enumerate(curr.neighbors):
                neighbor_clone=seen[neighbor] if neighbor in seen else Node(val=neighbor.val)
                clone.neighbors[i]=neighbor_clone

                if neighbor in seen: continue
                q.append((neighbor,neighbor_clone))
                seen[neighbor]=neighbor_clone

        return clone_node
            
