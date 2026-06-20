# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head

        start=ListNode(val=float('inf'))
        start.next=head

        slow=start
        fast=start
        #idx(old_terminal)-idx(new_terminal)=k
        i=0
        while i<k:
            if not fast.next: #restart with updated k
                k,fast=k%i,start
                i=0
            else:
                fast=fast.next
                i+=1
        if not fast.next: return head

        #fast=old terminal, slow=new terminal

        while fast.next:
            slow=slow.next
            fast=fast.next
        fast.next=start.next
        start.next=slow.next
        slow.next=None
        return start.next
        

