# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)

        current = dummy

        while current.next is not None and current.next.next is not None:
            if current.next.val != current.next.next.val:
                current = current.next

            else:
                val = current.next.val

                while current.next is not None and current.next.val == val:
                    current.next = current.next.next

        return dummy.next

