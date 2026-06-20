class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        M=len(nums)
        if M==1: return 

        k=k%M

        tail=[num for num in nums[-k:]]
        nums[k:]=nums[:-k]
        nums[0:k]=tail
        