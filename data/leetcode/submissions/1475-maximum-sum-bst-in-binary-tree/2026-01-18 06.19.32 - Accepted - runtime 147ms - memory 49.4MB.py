# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        '''
        stage_m: f*_m() subproblem solves the problem(max bst size) for node_m
        s_m: stingle state
        x_m: left and or right children
        f_m(x_m) = f*_{x_m}()
        f*_m = sum(f_m(x_m)) 

        '''

        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        self.maxVal=0

        SUM=0
        MIN=1
        MAX=2
        memo={}
        def dfs(node):
            if node in memo: return
            if not node:
                memo[node]= (0,float("inf"),-float("inf"))
                return
            if not node.left and not node.right:
                self.maxVal=max(self.maxVal, node.val)
                memo[node]= (node.val, node.val, node.val)
                return

            _,_=dfs(node.left),dfs(node.right)

            bad_L=node.left and not (memo[node.left][MAX] < node.val)
            bad_R=node.right and not (memo[node.right][MIN] > node.val)
            if bad_L or bad_R:
                f_max= (-float("inf"), float("inf"), -float("inf"))
                memo[node]=f_max
            else:
                f_max = (
                    node.val + memo[node.left][SUM] + memo[node.right][SUM], 
                    min(node.val, memo[node.left][MIN]), 
                    max(node.val, memo[node.right][MAX])
                    )
                memo[node]=f_max
            self.maxVal=max(self.maxVal, memo[node][SUM])
   
        dfs(root)
        return self.maxVal

        