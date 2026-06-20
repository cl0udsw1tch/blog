# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        start=ListNode(val=float('inf'))
        start.next=head
        prev=start

        slow_prev=None
        slow=start
        i=0
        while i<n:
            prev=prev.next
            i+=1

        fast=prev
        while fast:
            slow_prev=slow
            slow=slow.next
            fast=fast.next

        slow_prev.next=slow.next
        return start.next

        