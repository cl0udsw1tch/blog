# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        '''
        stage_m: subproblem f_m(s_m, t_m) solves the problem at node-m and a camera placed at it's parent and itself
        s_m: no camera (0) or camera (1) at parent
        t_m: no camera (0) or camera (1) at itself
        x_m: camera or no camera at each child
        f_m(s_m, t_m, x_m) = t_m + f*_{ml}(t_m, x_m for left child) + f*_{mr}(t_m, x_m for right child) 
        f*_m(t_m, s_m) = min_{x_m}(f_m(t_m, s_m, x_m))
        '''

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        memo={}
        X=[(False, True), (True, False), (True, True)]

        def dfs(s):
            if s in memo: return
            node,s_parent,s_node=s
            if not node:
                memo[s]=0 if not s_node else float('inf')
                return
            if not node.left and not node.right:
                if s_node:
                    memo[s]=1
                elif not s_node and s_parent:
                    memo[s]=0
                elif not s_node and not s_parent:
                    memo[s]=float('inf')
                return
            F=float('inf')
            if s_parent or s_node:
                s_pl,s_pr=(node.left, s_node, False),(node.right, s_node, False)
                _,_=dfs(s_pl),dfs(s_pr)
                F=min(F,int(s_node)+memo[s_pl]+memo[s_pr])
            
            for s_child_l, s_child_r in X:
 
                s_pl,s_pr=(node.left, s_node, s_child_l),(node.right, s_node, s_child_r)
                _,_=dfs(s_pl),dfs(s_pr)
                F=min(F,int(s_node)+memo[s_pl]+memo[s_pr])
      
            memo[s]=F
            
        s1,s2=(root,False, False),(root,False, True)
        _,_=dfs(s1),dfs(s2)
        return min(memo[s1],memo[s2])

        