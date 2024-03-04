class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # slow = head
    # fast = head

    # for _ in range(n):
    #   fast = fast.next
    # if not fast:
    #   return head.next

    # while fast.next:
    #   slow = slow.next
    #   fast = fast.next
    # slow.next = slow.next.next

    # return head

    dummy = ListNode(0,head)
    left = dummy
    right = head

    while n>0 and right:
        right=right.next
        n-=1
    while right:
        right = right.next
        left = left.next
    left.next = left.next.next
    return dummy.next


