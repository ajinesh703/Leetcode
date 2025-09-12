# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        size: int = 0
        output: ListNode = ListNode(next=head)
        tmp: ListNode = output
        l: ListNode = head
        r: ListNode = head
        while size < right:
            size += 1
            if size < left:
                tmp = tmp.next
                l = l.next
            r = r.next
        for _ in range(right - left):
            tmp.next = l.next
            l.next = r
            r = l
            l = tmp.next
        l.next = r
        return output.next
