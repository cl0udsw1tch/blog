# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        return mergesort(head)

def mergesort(head):
    if not head: return head
    if not head.next: return head

    prev,fast=None,head
    while fast and fast.next:
        prev=prev.next if prev else head
        fast=fast.next.next

    prev_next=prev.next
    prev.next=None
    h1,h2=mergesort(head),mergesort(prev_next)
    prev1,ptr1,ptr2=None,h1,h2
    
    while ptr1 and ptr2:
        if ptr2.val<ptr1.val:
            ptr2_next=ptr2.next
            if prev1:
                prev1.next=ptr2
            prev1=ptr2
            ptr2.next=ptr1
            ptr2=ptr2_next
        else:
            prev1=prev1.next if prev1 else h1
            ptr1=ptr1.next
    prev1.next=ptr1 if ptr1 else ptr2

    return h2 if h2.val<h1.val else h1

def quicksort(lo, hi):
    if lo==hi: return lo,hi

    head,pivot_prev,tail=partition(lo,hi)
    
    pivot=pivot_prev.next
    pivot_next=pivot.next
    pivot_prev.next=None

    if pivot==head:
        head1,tail1=pivot,pivot
        head2,tail2=quicksort(pivot_next,tail)
        tail1.next=head2
        return head1,tail2
    elif pivot==tail:
        head1,tail1=quicksort(head,pivot_prev)
        head2,tail2=pivot,pivot
        tail1.next=tail2
        return head1,tail2
    else:
        head1,tail1=quicksort(head,pivot_prev)
        head2,tail2=quicksort(pivot_next,tail)
        tail1.next=pivot
        tail1.next.next=head2
        return head1,tail2

def partition(head,tail): # returns head, pivot predecessor, tail
    start=ListNode()
    start.next=head

    if not head.next.next:
        if head.val>head.next.val:
            t=swap(start, head)
            return start.next,start.next,t
        return start.next,start.next,head.next

    pivot_val=tail.val

    prev,curr=start,head
    pivot_prev,pivot=start,head
    while curr.next:
        if curr.val<=pivot_val:
            if curr==pivot:
                prev,curr=prev.next,curr.next
                pivot_prev,pivot=pivot_prev.next,pivot.next
            else:
                t=swap(pivot_prev,prev)
                pivot_prev=pivot_prev.next
                pivot=pivot_prev.next
                prev=t
                curr=prev.next
        else:
            prev=curr
            curr=curr.next
    t=swap(pivot_prev,prev)

    return start.next,pivot_prev,t


def swap(prev_a, prev_b):
    
    a,b=prev_a.next,prev_b.next
    if a.next==b:
        # prev_a -> a == prev_b -> b
        b_next=b.next
        prev_a.next=b
        b.next=a
        a.next=b_next
        return a
    
    # prev_a -> a ..-> prev_b -> b
    b_next=b.next
    prev_a.next=b
    b.next=a.next
    prev_b.next=a
    a.next=b_next

    return a


    