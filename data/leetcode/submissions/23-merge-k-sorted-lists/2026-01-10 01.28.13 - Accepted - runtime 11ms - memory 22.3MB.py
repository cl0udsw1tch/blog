# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        N=len(lists)
        if N==0: return None
        if N==1: return lists[0]

        def DandC(lo,hi):
            assert(lo<=hi)
            if lo+1==hi: return lists[lo]

            MID=(hi-lo)//2+lo
            h1,h2=(DandC(lo,MID),DandC(MID,hi)) if hi>lo+2 else (lists[lo],lists[hi-1])

            if not h1: return h2
            if not h2: return h1

            prev=None
            ptr1,ptr2=h1,h2
            while ptr1 and ptr2:
                if ptr2.val<ptr1.val:
                    ptr2_next=ptr2.next
                    ptr2.next=ptr1
                    if prev:
                        prev.next=ptr2
                    prev=ptr2
                    ptr2=ptr2_next
                else:
                    prev=ptr1
                    ptr1=ptr1.next
            prev.next=ptr1 if ptr1 else ptr2
            return h2 if h2.val < h1.val else h1

        return DandC(0,N)
    
