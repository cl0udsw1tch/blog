# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        '''
        stage_m: 0...M-1 subproblem f*_m() solves the problem for tree with root m
        s_m: rob, not rob
        x_m: rob only m, rob only left, rob only right, rob both left and right, rob neither (feasibility considered)
        f_m(rob) = m.val + f*_{mr}(not-rob) + f*_{ml}(not-rob)
        f_m(not-rob) = max(f*_{mr}(not-rob) + f*_{ml}(rob), f*_{mr}(rob) + f*_{ml}(not-rob),
        max(f*_{mr}(rob) + f*_{ml}(rob), f*_{mr}(not-rob) + f*_{ml}(not-rob)
        )

        f*_m(s_m) = max_{x_m}(f_m(s_m, x_m))
        '''

        if not root.left and not root.right:
            return root.val

        memo={None: (0,0)}
        def dfs(node):
            if node in memo:
                return

            if not node.left and not node.right:
                memo[node]=node.val,0
                return
   

            dfs(node.left)
            dfs(node.right)

            rob_left,skip_left=memo[node.left]
            rob_right,skip_right=memo[node.right]

            F1=node.val+skip_left+skip_right
            F2=max(
                rob_left + rob_right, 
                rob_left + skip_right, 
                skip_left + rob_right, 
                skip_left + skip_right
                )

            memo[node]=F1,F2

        dfs(root)
        return max(memo[root])
                

