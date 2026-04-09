# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #1 find length

        c = 0
        cur = head

        while cur:
            c += 1
            cur = cur.next

        #2. temp head <- uses a new ListNode def

        temp = ListNode(0, head) #this is the old head again
        cur = temp #(basically the head piece again)

        for r in range(c-n): 
            cur = cur.next
        
        cur.next = cur.next.next

        return temp.next
        