# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        
        while head:
            node = head
            head = head.next
            
            current = dummy
            
            while current.next and node.val > current.next.val:
                current = current.next
                
            node.next = current.next
            current.next = node
            
        return dummy.next
