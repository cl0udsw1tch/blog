
class __2Max__:
    first=None
    second=None
    def __init__(self):
        self.first=-float('inf')
        self.second=-float('inf')
    def push(self, val):

        if val>self.first:
            self.second=self.first
            self.first=val
        elif val>self.second:
            self.second=val

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:

        if n==1:
            return 0
        graph=[[] for _ in range(n)]
        for edge in edges:
            a,b=tuple(edge)
            graph[a].append(b)
            graph[b].append(a)

        within_subtree={}
        within_sibling_tree={}
        outside_subtree={}

        def dfs_within_subtree(node, parent=None):
            if node in within_subtree:
                return
            d=__2Max__()
            d.push(price[node])
            for nbr in graph[node]:
                if nbr==parent: continue
                dfs_within_subtree(nbr, node)
                d.push(price[node]+within_subtree[nbr])
            
            within_subtree[node]=d.first
            within_sibling_tree[node]=d.second

        def dfs_outside_subtree(node, parent=None):
            if node in outside_subtree:
                return 
            if parent is None:
                outside_subtree[node]=price[node]
            else:
                is_max_branch=((within_subtree[node]+price[parent])==within_subtree[parent])
                outside_subtree[node]=max(
                    price[node]+(within_sibling_tree if is_max_branch else within_subtree)[parent], 
                    price[node]+outside_subtree[parent]
                    )
            for nbr in graph[node]: 
                if nbr==parent: continue
                dfs_outside_subtree(nbr, node)
        
        dfs_within_subtree(0,None)
        dfs_outside_subtree(0,None)
        subtree_max=max([within_subtree[node]-price[node] for node in range(n)])
        out_max=max([outside_subtree[node]-price[node] for node in range(n)])
        return max(subtree_max, out_max)



