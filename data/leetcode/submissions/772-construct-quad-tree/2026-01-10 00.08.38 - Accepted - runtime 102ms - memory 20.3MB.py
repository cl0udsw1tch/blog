"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N=len(grid)
        X=['topLeft','topRight','bottomLeft','bottomRight']
        def DandC(i,j,sz):
            if sz==1:
                return Node(grid[i][j], True, None,None,None,None)
            
            node=Node(0,False,None,None,None,None)
            c=0
            all_children_leaves=True
            all_children_same=True
            for x in range(0,sz,sz//2):
                for y in range(0,sz,sz//2):
                    i_p,j_p,sz_p=i+x,j+y,sz//2
                    child=DandC(i_p,j_p,sz_p)
                    setattr(node,X[c],child)
                    all_children_same=c==0 or (all_children_same and child.val==getattr(node,X[c-1]).val)
                    if not child.isLeaf: all_children_leaves=False
                    c+=1
            if all_children_leaves:
                node.isLeaf=all_children_same
            if node.isLeaf:
                node.val=node.topLeft.val
                for idx,x in enumerate(X):
                    setattr(node,x,None)
            return node
        return DandC(0,0,N)