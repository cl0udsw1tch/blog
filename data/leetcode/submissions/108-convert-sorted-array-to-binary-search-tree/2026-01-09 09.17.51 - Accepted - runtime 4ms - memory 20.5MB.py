# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        M=len(nums)
        if M==0: return None
        if M==1: return TreeNode(val=nums[0])
        if M==2:
            return TreeNode(val=nums[1], left=TreeNode(val=nums[0]))
        if M==3:
            return TreeNode(val=nums[1], left=TreeNode(val=nums[0]),right=TreeNode(val=nums[2]))

        left,middle,right=nums[:M//2],nums[M//2],nums[M//2+1:]
        root=TreeNode(val=middle)
        root.left,root.right=self.sortedArrayToBST(left),self.sortedArrayToBST(right)
        return root

