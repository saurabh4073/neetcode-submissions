# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev,slow2 = None, slow.next
        slow.next = None

        while slow2:
            tmp = slow2.next
            slow2.next = prev
            prev= slow2
            slow2=tmp
        
        first,second= head,prev
        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second= tmp1,tmp2