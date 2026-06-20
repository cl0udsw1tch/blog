class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n==0:
            return

        i,j,k=m-1,n-1,m+n-1
   
        while i>-1 and j>-1:
            a,b=nums1[i],nums2[j]
            if a>b:
                nums1[k]=a
                i-=1
            else:
                nums1[k]=b
                j-=1
            k-=1
        while j>-1:
            nums1[k]=nums2[j]
            k-=1
            j-=1


        