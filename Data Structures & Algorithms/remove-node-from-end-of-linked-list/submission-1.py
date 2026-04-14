# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        c = 0
        curr = head

        while curr:
            c += 1
            curr = curr.next

        
        temp = ListNode(0, head)
        cur = temp

        for r in range(c-n):
            cur = cur.next

        cur.next = cur.next.next

        return temp.next