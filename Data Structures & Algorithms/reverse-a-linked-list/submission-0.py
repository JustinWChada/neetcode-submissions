# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        prev_node = None

        if not node:
            return 

        while node.next:
            curr_node = node
            next_node = node.next

            curr_node.next = prev_node
            prev_node = curr_node
            node = next_node
        
        node.next = prev_node

        return node

