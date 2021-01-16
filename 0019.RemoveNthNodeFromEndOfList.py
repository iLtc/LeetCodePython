# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        current = head
        
        while current != None:
            size += 1
            current = current.next
            
        dummy = ListNode(next=head)
        
        left = dummy
        right = head
        
        for _ in range(size - n):
            left = left.next
            right = right.next
            
        left.next = left.next.next
            
        return dummy.next
