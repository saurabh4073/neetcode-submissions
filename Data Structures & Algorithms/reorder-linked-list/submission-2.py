# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev,slow2=None,slow.next
        slow.next = None
        while slow2:
            tmp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = tmp
        
        one , two = head, prev
        while two:
            tmp = one.next
            tmp2 = two.next
            one.next = two
            two.next=tmp
            one,two = tmp,tmp2