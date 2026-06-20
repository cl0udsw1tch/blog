# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False
        ptr1,ptr2=head,head.next

        while ptr2 is not None:
            if ptr1==ptr2: return True

            ptr1=ptr1.next

            ptr2=ptr2.next
            if ptr2 is None: return False
            ptr2=ptr2.next


        return False