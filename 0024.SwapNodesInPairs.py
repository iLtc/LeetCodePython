# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)

        first = dummy

        while first is not None and first.next is not None and first.next.next is not None:
            second = first.next
            third = second.next

            second.next = third.next
            third.next = second
            first.next = third

            first = second

        return dummy.next

