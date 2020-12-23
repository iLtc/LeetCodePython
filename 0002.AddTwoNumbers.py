# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        carry = val // 10
        head = ListNode(val % 10)
        
        current = head
        
        while l1.next is not None or l2.next is not None or carry > 0:
            if l1.next is None:
                l1.next = ListNode(0)
                
            if l2.next is None:
                l2.next = ListNode(0)
                
            val = l1.next.val + l2.next.val + carry
            carry = val // 10
            current.next = ListNode(val % 10)
            
            l1 = l1.next
            l2 = l2.next
            current = current.next
            
        return head
