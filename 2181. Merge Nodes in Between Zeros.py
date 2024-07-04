# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum =0
        output=ListNode()
        res_head = output
        cur = head.next
        while cur:
            if cur.val != 0:
                sum+=cur.val
            else:
                new_node =ListNode()
                new_node.val = sum 
                output.next = new_node
                sum=0
                output = output.next
            cur = cur.next
        return res_head.next