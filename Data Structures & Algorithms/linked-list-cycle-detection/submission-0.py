# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head


        #if self.val in seen: self.val not a thing use head
        #also needs a end point while
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False